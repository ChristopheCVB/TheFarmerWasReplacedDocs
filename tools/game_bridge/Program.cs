using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.Loader;
using System.Text.Json;
using Mono.Cecil;
using Mono.Cecil.Cil;
using UnityEngine;
using N = System.Numerics;
using UObject = UnityEngine.Object;

public static class Shim
{
    public sealed class SliceComplete : Exception { }
    public static bool YieldSlice(object gate) => throw new SliceComplete();
    public static readonly Dictionary<object, JsonElement> Curves = new(ReferenceEqualityComparer.Instance);
    public static readonly Dictionary<object, string> Names = new(ReferenceEqualityComparer.Instance);
    public static readonly Dictionary<object, int> Ids = new(ReferenceEqualityComparer.Instance);
    static readonly Dictionary<IntPtr, JsonElement> GeneratedCurves = new();
    static readonly Dictionary<object, GradientColorKey[]> GeneratedGradients = new(ReferenceEqualityComparer.Instance);
    static int nextId;
    public static UObject[] Resources = Array.Empty<UObject>();
    public static UObject[] LoadAllResources(string path, Type type) => Resources.Where(type.IsInstanceOfType).ToArray();
    public static UObject LoadResource(string path, Type type) => Resources.SingleOrDefault(o => type.IsInstanceOfType(o) && string.Equals(Names.GetValueOrDefault(o), Path.GetFileName(path), StringComparison.OrdinalIgnoreCase))
        ?? throw new NotSupportedException("Missing offline resource: " + path);
    public static ScriptableObject CreateSO(Type type, bool applyDefaultsAndReset)
    {
        var value = (ScriptableObject)Activator.CreateInstance(type);
        if (applyDefaultsAndReset) type.GetMethod("OnEnable", BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic)?.Invoke(value, null);
        return value;
    }
    public static UObject Clone(UObject original)
    {
        object Copy(object v, bool root = false)
        {
            if (v == null) return null; var t = v.GetType();
            if (t.IsPrimitive || t.IsEnum || t == typeof(string) || v is UObject && !root) return v;
            if (v is AnimationCurve || v is Gradient)
            {
                var c = RuntimeHelpers.GetUninitializedObject(t);
                if (Curves.TryGetValue(v, out var curve)) Curves[c] = curve;
                if (v is Gradient && GeneratedGradients.TryGetValue(v, out var keys))
                    GeneratedGradients[c] = (GradientColorKey[])keys.Clone();
                return c;
            }
            if (v is Array a) { var c = Array.CreateInstance(t.GetElementType(), a.Length); for (int i = 0; i < a.Length; i++) c.SetValue(Copy(a.GetValue(i)), i); return c; }
            if (v is System.Collections.IList list) { var c = (System.Collections.IList)Activator.CreateInstance(t); foreach (var item in list) c.Add(Copy(item)); return c; }
            var result = Activator.CreateInstance(t);
            foreach (var f in t.GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic))
                if (!f.IsNotSerialized && (f.IsPublic || f.IsDefined(typeof(SerializeField))))
                    f.SetValue(result, Copy(f.GetValue(v)));
            return result;
        }
        var clone = (UObject)Copy(original, true); Init(clone); Names[clone] = Names.GetValueOrDefault(original, ""); return clone;
    }
    public static void Init(UObject o)
    {
        typeof(UObject).GetField("m_CachedPtr", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(o, new IntPtr(1));
        Ids[o] = ++nextId;
    }
    public static string Name(UObject o) => Names.GetValueOrDefault(o, "");
    public static void NameSet(UObject o, string n) => Names[o] = n;
    public static bool MainThread() => true;
    public static int Zero() => 0;
    public static int ObjectId(UObject o) => Ids[o];
    public static string DataPath() => Path.GetTempPath();
    public static void UnityLog(LogType level, LogOption options, string message, UObject context)
    {
        if (level is LogType.Error or LogType.Exception or LogType.Assert)
            throw new NotSupportedException("Engine diagnostic: " + message);
    }
    public static IntPtr CreateCurve(Keyframe[] keys)
    {
        var id = new IntPtr(++nextId); GeneratedCurves[id] = JsonSerializer.SerializeToElement(new { m_Curve = (keys ?? Array.Empty<Keyframe>()).Select(k => new { time = k.time, value = k.value, inSlope = k.inTangent, outSlope = k.outTangent, weightedMode = (int)k.weightedMode }) }); return id;
    }
    public static void DestroyCurve(IntPtr id) { GeneratedCurves.Remove(id); }
    public static IntPtr CreateGradient() => new(++nextId);
    public static void CleanupGradient(Gradient g) { GeneratedGradients.Remove(g); }
    public static void GradientKeys(Gradient g, GradientColorKey[] colors, GradientAlphaKey[] alphas) => GeneratedGradients[g] = colors;
    public static void GradientModeSet(Gradient g, GradientMode mode) { if (mode != GradientMode.Blend) throw new NotSupportedException("Nonlinear gradient mode"); }
    public static float CurveEvaluate(AnimationCurve c, float time)
    {
        var data = Curves.TryGetValue(c, out var stored) ? stored : GeneratedCurves[(IntPtr)typeof(AnimationCurve).GetField("m_Ptr", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(c)];
        var keys = data.GetProperty("m_Curve").EnumerateArray().ToArray();
        if (keys.Length == 0) return 0;
        float F(JsonElement k, string n) => k.GetProperty(n).GetSingle();
        if (time <= F(keys[0], "time")) return F(keys[0], "value");
        for (int i = 1; i < keys.Length; i++)
        {
            var a = keys[i - 1]; var b = keys[i];
            if (time > F(b, "time")) continue;
            if (a.GetProperty("weightedMode").GetInt32() != 0 || b.GetProperty("weightedMode").GetInt32() != 0)
                throw new NotSupportedException("Weighted animation curves");
            float dt = F(b, "time") - F(a, "time"), t = (time - F(a, "time")) / dt;
            if (float.IsInfinity(F(a, "outSlope"))) return F(a, "value");
            return (2 * t * t * t - 3 * t * t + 1) * F(a, "value") + (t * t * t - 2 * t * t + t) * dt * F(a, "outSlope")
                 + (-2 * t * t * t + 3 * t * t) * F(b, "value") + (t * t * t - t * t) * dt * F(b, "inSlope");
        }
        return F(keys[^1], "value");
    }
    public static Color GradientEvaluate(Gradient g, float time)
    {
        if (GeneratedGradients.TryGetValue(g, out var colors))
        {
            if (colors.Length == 0) return Color.white;
            for (int i = 1; i < colors.Length; i++) if (time <= colors[i].time) return Color.Lerp(colors[i - 1].color, colors[i].color, (time - colors[i - 1].time) / (colors[i].time - colors[i - 1].time));
            return colors[^1].color;
        }
        var j = Curves[g]; int count = j.GetProperty("m_NumColorKeys").GetInt32();
        Color C(int i) { var c = j.GetProperty("key" + i); return new(c.GetProperty("r").GetSingle(), c.GetProperty("g").GetSingle(), c.GetProperty("b").GetSingle(), 1); }
        if (count == 0) return Color.white;
        for (int i = 1; i < count; i++) { float end = j.GetProperty("ctime" + i).GetSingle() / 65535f; if (time > end) continue; float start = j.GetProperty("ctime" + (i - 1)).GetSingle() / 65535f; return Color.Lerp(C(i - 1), C(i), (time - start) / (end - start)); }
        return C(count - 1);
    }
    static N.Quaternion Q(Quaternion q) => new(q.x, q.y, q.z, q.w);
    static Quaternion U(N.Quaternion q) => new(q.X, q.Y, q.Z, q.W);
    public static Quaternion Slerp(Quaternion a, Quaternion b, float t) => U(N.Quaternion.Slerp(Q(a), Q(b), Math.Clamp(t, 0, 1)));
    public static Quaternion SlerpUnclamped(Quaternion a, Quaternion b, float t) => U(N.Quaternion.Slerp(Q(a), Q(b), t));
    public static Quaternion EulerRad(Vector3 v) => U(N.Quaternion.CreateFromAxisAngle(N.Vector3.UnitY, v.y) * N.Quaternion.CreateFromAxisAngle(N.Vector3.UnitX, v.x) * N.Quaternion.CreateFromAxisAngle(N.Vector3.UnitZ, v.z));
    public static Quaternion AngleAxis(float a, Vector3 v) => U(N.Quaternion.CreateFromAxisAngle(N.Vector3.Normalize(new(v.x, v.y, v.z)), a * MathF.PI / 180));
    public static Quaternion LookRotation(Vector3 forward, Vector3 up)
    {
        var z = N.Vector3.Normalize(new(forward.x, forward.y, forward.z)); var x = N.Vector3.Normalize(N.Vector3.Cross(new(up.x, up.y, up.z), z)); var y = N.Vector3.Cross(z, x);
        return U(N.Quaternion.CreateFromRotationMatrix(new(x.X, x.Y, x.Z, 0, y.X, y.Y, y.Z, 0, z.X, z.Y, z.Z, 0, 0, 0, 0, 1)));
    }
    public static Matrix4x4 TRS(Vector3 p, Quaternion q, Vector3 s)
    {
        var a = N.Matrix4x4.CreateScale(s.x, s.y, s.z) * N.Matrix4x4.CreateFromQuaternion(Q(q)) * N.Matrix4x4.CreateTranslation(p.x, p.y, p.z);
        return new(new(a.M11, a.M12, a.M13, a.M14), new(a.M21, a.M22, a.M23, a.M24), new(a.M31, a.M32, a.M33, a.M34), new(a.M41, a.M42, a.M43, a.M44));
    }
    static N.Matrix4x4 Numeric(Matrix4x4 m) => new(m.m00, m.m10, m.m20, m.m30, m.m01, m.m11, m.m21, m.m31, m.m02, m.m12, m.m22, m.m32, m.m03, m.m13, m.m23, m.m33);
    public static Quaternion MatrixRotation(ref Matrix4x4 m) { if (!N.Matrix4x4.Decompose(Numeric(m), out _, out var q, out _)) throw new NotSupportedException("Non-TRS matrix rotation"); return U(q); }
    public static Vector3 MatrixScale(ref Matrix4x4 m) { if (!N.Matrix4x4.Decompose(Numeric(m), out var s, out _, out _)) throw new NotSupportedException("Non-TRS matrix scale"); return new(s.X, s.Y, s.Z); }
}

public class Runner : ISimRunner
{
    public Transform SceneScaler => null;
    public Logger Logger { get; set; } = new(false);
    public int RenderLayer => 0;
    public Vector3 PiggyBankPosition => Vector3.zero;
    public RenderPackage GetRenderPackage() => throw new NotSupportedException("Unity renderer");
    public double TimeFactor { get; set; } = 1;
    public bool StepByStepMode { get; set; }
    public int HarvestFactor => 1;
    public bool RecordsAchievements => false;
    public Platforms.EDlcMask InstalledDlcs { get; set; }
    public void ScheduleLeaderboardStart(MainSim.LeaderboardStartArgs a) => throw new NotSupportedException("Leaderboard start");
    public void PlaySound(SoundEffectType t, Vector2Int p) { }
    public void PlayEffect(VFXType t, Vector3 p, bool b, Color c, string s, float x, float y) { }
    public void CollectItemEffect(int i, Vector3 p) { }
    public void CrumbleEffect(Vector3Int p) { }
    public void SlideBlockEffect(Vector2Int a, Vector2Int b) { }
    public void SlideAndPopBlockEffect(Vector2Int a, Vector2Int b, int x, int y) { }
    public void DelayedPopBlockEffect(Vector3Int p, float f, Vector3 v) { }
    public void BlinkEffect(Node n) { }
    public void SetDirty() { }
}

public static class Bridge
{
    static readonly BindingFlags Flags = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance;
    static readonly Dictionary<long, object> Objects = new();
    static string Root;
    public static int Main(string[] args)
    {
        try
        {
            Root = args[1];
            AssemblyLoadContext.Default.Resolving += (c, n) => { var p = Path.Combine(Root, n.Name + ".dll"); return File.Exists(p) ? c.LoadFromAssemblyPath(p) : null; };
            if (args[0] == "prepare") { Prepare(args[2]); return 0; }
            Run(args[2], args[3]); return 0;
        }
        catch (Exception e) { Console.Error.WriteLine(e); return 1; }
    }
    static void Prepare(string target)
    {
        var resolver = new DefaultAssemblyResolver(); resolver.AddSearchDirectory(Root); resolver.AddSearchDirectory(AppContext.BaseDirectory);
        using var asm = AssemblyDefinition.ReadAssembly(Path.Combine(Root, "UnityEngine.CoreModule.dll"), new ReaderParameters { AssemblyResolver = resolver });
        var map = new Dictionary<string, string>
        {
            ["UnityEngine.ScriptableObject::CreateScriptableObject"] = "Init",
            ["UnityEngine.ScriptableObject::CreateScriptableObjectInstanceFromType"] = "CreateSO",
            ["UnityEngine.Object::get_name"] = "Name",
            ["UnityEngine.Object::set_name"] = "NameSet",
            ["UnityEngine.Object::CurrentThreadIsMainThread"] = "MainThread",
            ["UnityEngine.Object::GetOffsetOfInstanceIDInCPlusPlusObject"] = "Zero",
            ["UnityEngine.Object::GetInstanceID"] = "ObjectId",
            ["UnityEngine.Object::Internal_CloneSingle"] = "Clone",
            ["UnityEngine.Application::get_persistentDataPath"] = "DataPath",
            ["UnityEngine.DebugLogHandler::Internal_Log"] = "UnityLog",
            ["UnityEngine.AnimationCurve::Evaluate"] = "CurveEvaluate",
            ["UnityEngine.AnimationCurve::Internal_Create"] = "CreateCurve",
            ["UnityEngine.AnimationCurve::Internal_Destroy"] = "DestroyCurve",
            ["UnityEngine.Gradient::Evaluate"] = "GradientEvaluate",
            ["UnityEngine.Gradient::Init"] = "CreateGradient",
            ["UnityEngine.Gradient::Cleanup"] = "CleanupGradient",
            ["UnityEngine.Gradient::SetKeys"] = "GradientKeys",
            ["UnityEngine.Gradient::set_mode"] = "GradientModeSet",
            ["UnityEngine.Quaternion::Slerp"] = "Slerp",
            ["UnityEngine.Quaternion::SlerpUnclamped"] = "SlerpUnclamped",
            ["UnityEngine.Quaternion::Internal_FromEulerRad"] = "EulerRad",
            ["UnityEngine.Quaternion::AngleAxis"] = "AngleAxis",
            ["UnityEngine.Quaternion::LookRotation"] = "LookRotation",
            ["UnityEngine.Matrix4x4::TRS"] = "TRS"
            ,
            ["UnityEngine.Matrix4x4::GetRotation"] = "MatrixRotation"
            ,
            ["UnityEngine.Matrix4x4::GetLossyScale"] = "MatrixScale"
            ,
            ["UnityEngine.ResourcesAPIInternal::LoadAll"] = "LoadAllResources"
            ,
            ["UnityEngine.ResourcesAPIInternal::Load"] = "LoadResource"
        };
        foreach (var t in asm.MainModule.Types) foreach (var m in t.Methods)
            {
                if (!map.TryGetValue(t.FullName + "::" + m.Name, out var name)) continue;
                var dest = typeof(Shim).GetMethod(name); if (m.Parameters.Count + (m.HasThis ? 1 : 0) != dest.GetParameters().Length) continue;
                m.IsPInvokeImpl = false; m.IsInternalCall = false; m.IsNative = false; m.IsManaged = true; m.IsIL = true;
                m.Body = new Mono.Cecil.Cil.MethodBody(m); var il = m.Body.GetILProcessor();
                for (int i = 0; i < dest.GetParameters().Length; i++) il.Emit(OpCodes.Ldarg, i);
                il.Emit(OpCodes.Call, asm.MainModule.ImportReference(dest)); il.Emit(OpCodes.Ret);
                Console.Error.WriteLine("Adapter " + t.FullName + "::" + m.Name);
            }
        asm.Write(target);
        using var core = AssemblyDefinition.ReadAssembly(Path.Combine(Root, "Core.dll"), new ReaderParameters { AssemblyResolver = resolver });
        var method = core.MainModule.Types.Single(t => t.Name == "Simulation").Methods.Single(m => m.Name == "RunNextStep");
        foreach (var i in method.Body.Instructions)
            if (i.Operand is MethodReference mr && mr.DeclaringType.FullName == "System.Threading.Monitor" && mr.Name == "Wait")
                i.Operand = core.MainModule.ImportReference(typeof(Shim).GetMethod("YieldSlice"));
        core.Write(Path.Combine(Path.GetDirectoryName(target), "Core.offline"));
    }
    static Type Resolve(string name) => typeof(Simulation).Assembly.GetType(name) ?? typeof(DesignConstants).Assembly.GetType(name) ?? typeof(UObject).Assembly.GetType(name) ?? typeof(AudioClip).Assembly.GetType(name);
    static object Read(JsonElement j, Type t)
    {
        if (j.ValueKind == JsonValueKind.Null) return null;
        if (j.ValueKind == JsonValueKind.Object && j.TryGetProperty("m_PathID", out var ptr))
        {
            if (ptr.GetInt64() == 0) return null;
            if (j.GetProperty("m_FileID").GetInt32() == 0 && Objects.TryGetValue(ptr.GetInt64(), out var value) && t.IsInstanceOfType(value)) return value;
            if (typeof(ScriptableObject).IsAssignableFrom(t)) throw new NotSupportedException("Unresolved gameplay resource: " + t.Name);
            // Visual effects reference scene prefabs; the offline runner doesn't create them.
            return null;
        }
        if (t == typeof(string)) return j.GetString();
        if (t == typeof(bool)) return j.ValueKind == JsonValueKind.True || j.ValueKind == JsonValueKind.Number && j.GetInt32() != 0;
        if (t.IsEnum) return Enum.ToObject(t, j.GetInt32());
        if (t.IsPrimitive) return Convert.ChangeType(j.GetDouble(), t);
        if (t.IsArray) { var a = Array.CreateInstance(t.GetElementType(), j.GetArrayLength()); int i = 0; foreach (var v in j.EnumerateArray()) a.SetValue(Read(v, t.GetElementType()), i++); return a; }
        if (t.IsGenericType && t.GetGenericTypeDefinition() == typeof(List<>)) { var a = (System.Collections.IList)Activator.CreateInstance(t); foreach (var v in j.EnumerateArray()) a.Add(Read(v, t.GetGenericArguments()[0])); return a; }
        if (t == typeof(AnimationCurve) || t == typeof(Gradient)) { var c = RuntimeHelpers.GetUninitializedObject(t); Shim.Curves[c] = j.Clone(); return c; }
        var obj = Activator.CreateInstance(t);
        foreach (var p in j.EnumerateObject()) { var f = t.GetField(p.Name, Flags); if (f != null && !f.IsStatic) f.SetValue(obj, Read(p.Value, f.FieldType)); }
        return obj;
    }
    static void LoadResources(string path)
    {
        using var doc = JsonDocument.Parse(File.ReadAllText(path));
        foreach (var j in doc.RootElement.EnumerateArray())
        {
            var t = Resolve(j.GetProperty("type").GetString()); if (t == null) continue;
            var obj = t == typeof(Mesh) || t == typeof(AudioClip) || t == typeof(Material) ? RuntimeHelpers.GetUninitializedObject(t) : Activator.CreateInstance(t); Objects[j.GetProperty("id").GetInt64()] = obj;
            if (obj is UObject u) { Shim.Init(u); Shim.Names[u] = j.GetProperty("data").GetProperty("m_Name").GetString(); }
        }
        foreach (var j in doc.RootElement.EnumerateArray())
        {
            if (!Objects.TryGetValue(j.GetProperty("id").GetInt64(), out var obj)) continue;
            foreach (var p in j.GetProperty("data").EnumerateObject()) { var f = obj.GetType().GetField(p.Name, Flags); if (f != null && !f.IsStatic) f.SetValue(obj, Read(p.Value, f.FieldType)); }
        }
        Shim.Resources = Objects.Values.OfType<UObject>().ToArray();
        var design = Objects.Values.OfType<DesignConstants>().Single(); typeof(DesignConstants).GetField("<Inst>k__BackingField", Flags).SetValue(null, design);
        foreach (var o in Objects.Values) { var m = o.GetType().GetMethod("OnEnable", Flags); if (m != null) m.Invoke(o, null); }
        ResourceManager.LoadAll();
        typeof(DesignConstants).GetMethod("Start", Flags)?.Invoke(design, null);
        var main = (MainSim)RuntimeHelpers.GetUninitializedObject(typeof(MainSim)); Shim.Init(main); main.harvestFactor = 1;
        typeof(MainSim).GetField("_instance", Flags).SetValue(null, main);
    }
    static float[] Matrix(Matrix4x4 m) => Enumerable.Range(0, 16).Select(i => m[i / 4, i % 4]).ToArray();
    static float[] Vector(Vector3 p) => new[] { p.x, p.y, p.z };
    static float[] ColorArray(Color c) => new[] { c.r, c.g, c.b, 1f };
    static Dictionary<object, long> PathIds;
    static long MeshId(Mesh m) => m is null ? throw new NotSupportedException("Missing mesh reference") : PathIds[m];
    static object Snapshot(Simulation sim, Runner runner)
    {
        var grid = sim.farm.grid; var tiles = new List<object>(); var meshes = new List<object>();
        for (int y = 0; y < grid.WorldSize.y; y++) for (int x = 0; x < grid.WorldSize.x; x++)
            {
                var cell = grid.CellAt(new Vector2Int(x, y)); var ground = grid.GroundAt(x, y, cell.depth);
                tiles.Add(new { x, y, depth = cell.depth, ground = ground.groundSo.objectName, color = ColorArray(ground.GetColor()), hardness = ground.hardness, stability = ground.stability, entity = cell.entity?.objectSO.objectName });
                if (cell.entity != null) foreach (var (mesh, matrix) in cell.entity.GetMeshes()) meshes.Add(new { id = MeshId(mesh), matrix = Matrix(matrix) });
            }
        var drones = sim.farm.drones.Where(d => d != null).Select(d =>
        {
            d.TryUpdateHeight(-1);
            return new { id = MeshId(d.hat.hatSO.hatMesh), matrix = Matrix(d.GetTransform()), digging = d.GetDiggingTimeRemaining(), position = new[] { d.pos.x, d.pos.y, d.depth }, hat = d.hat.hatSO.hatName };
        }).ToArray();
        var inventory = ResourceManager.GetAllItems().ToDictionary(i => i.itemName, i => sim.farm.Items.GetNumber(i.itemId));
        return new { time = sim.CurrentTime.Seconds, executing = sim.IsExecuting(), tiles, meshes, drones, inventory, output = runner.Logger.GetOutputString() };
    }
    static void Slice(Simulation sim, Duration target, object gate, bool setup = false)
    {
        try { while (true) sim.RunNextStep(target, gate, setup); }
        catch (Shim.SliceComplete) { if (!setup && sim.CurrentTime < target) throw new InvalidOperationException("Unexpected simulator yield"); }
    }
    static void Start(Simulation sim, string code)
    {
        Tokenizer.Tokenize(code + "\n", out var tokens);
        var window = (CodeWindow)RuntimeHelpers.GetUninitializedObject(typeof(CodeWindow)); Shim.Init(window);
        var functions = typeof(CodeWindow).GetField("parsedFunctions", Flags); functions.SetValue(window, Activator.CreateInstance(functions.FieldType));
        var program = Parser.Parse(tokens, window); sim.StartProgramExecution(new Execution(sim, program.syntaxTree, 0));
    }
    static void Run(string resources, string requestPath)
    {
        LoadResources(resources); PathIds = Objects.ToDictionary(k => k.Value, v => v.Key, ReferenceEqualityComparer.Instance);
        using var doc = JsonDocument.Parse(File.ReadAllText(requestPath)); var request = doc.RootElement;
        var settings = JsonSerializer.Deserialize<CodeExample.CodeExampleSettings>(request.GetProperty("config").GetRawText(), new JsonSerializerOptions { IncludeFields = true });
        var runner = new Runner { InstalledDlcs = (Platforms.EDlcMask)(settings.dlc_enabled ? 1 : 0) };
        var excluded = settings.exclude_unlocks.ToHashSet();
        var unlocks = ResourceManager.GetAllUnlocks().Where(u => !excluded.Contains(u.unlockName))
            .Select(u => u.IsMultiUnlock && string.IsNullOrEmpty(u.gainResource) && u.unlockName != "watering" ? $"{u.unlockName}_{u.maxUnlockLevel}" : u.unlockName)
            .Concat(ResourceManager.GetAllHats().Select(h => h.hatName));
        var items = ItemBlock.CreateEmpty(); foreach (var i in settings.items) items.AddItem(StringIds.GetItemId(i.item), i.n);
        int seed = settings.seed < 0 ? System.Security.Cryptography.RandomNumberGenerator.GetInt32(int.MaxValue) : settings.seed;
        var sim = new Simulation(runner, runner.InstalledDlcs, unlocks, items, "", "", (LeaderboardType)0, true, seed, null, null, false, settings.action_ticks, settings.operation_ticks, settings.world_size, settings.starting_chunk, null, null, null);
        typeof(MainSim).GetField("sim", Flags).SetValue(MainSim.Inst, sim);
        var gate = new object(); Start(sim, request.GetProperty("setup").GetString()); Slice(sim, sim.CurrentTime + Duration.FromSeconds(1000), gate, true);
        if (sim.IsExecuting()) throw new NotSupportedException("Setup exceeds 1000 simulation seconds");
        double start = sim.CurrentTime.Seconds; runner.Logger = new(false); Start(sim, request.GetProperty("code").GetString());
        var execution = sim.Execution;
        sim.ChangeExecutionSpeed(settings.execution_speed); sim.ChangeDiggingSpeed(settings.digging_speed);
        var frames = new List<object>(); int? done = null;
        for (int frame = 0; frame < 225; frame++)
        {
            Slice(sim, Duration.FromSeconds(start + frame / 15.0), gate);
            if (!sim.IsExecuting() && done == null)
            {
                done = frame;
                if (settings.print_last_result) runner.Logger.Log(execution.MainState.ReturnValue.ToString());
            }
            frames.Add(Snapshot(sim, runner)); if (done != null && frame >= done + 14) break;
        }
        Console.WriteLine(JsonSerializer.Serialize(new { seed, completed = done != null, frames }));
    }
}
