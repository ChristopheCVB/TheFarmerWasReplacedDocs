[Documentation index](../README.md)

# Exporter maintenance and validation

## Sources

Text: `TheFarmerWasReplaced_Data/StreamingAssets/Languages/EN/docs/` and the six
gameplay reference files in `EN/Strings/`. Illustrations and gameplay records:
`resources.assets`, its external stream, and script metadata from `globalgamemanagers.assets`.
Serialized field layouts were recovered from `Managed/Core.dll` and `Managed/Utils.dll`.
The extraction manifest records the Unity version, UTC export timestamp, source hashes,
and source-entry coverage. All source paths are relative to the installation.

## Regeneration

Requires **Python 3.10 or later**, with no third-party packages.
The reader supports the installed build and validates its Unity version and assembly hashes.

From the collection's root directory, substitute the game installation directory:

```sh
python tools/export_docs.py --game-dir /path/to/game
python tools/test_export.py
```

Output defaults to this directory. Use `--output` to generate a separate collection.
Existing generated pages are overwritten; unrelated files are not removed.
The installation is read only. Only the exported collection is written.

To validate an existing collection without exporting:

```sh
python tools/export_docs.py --validate-only
```

## Optional example output and animations

The media generator runs the installed game's managed interpreter and simulator outside Unity.
It loads extracted gameplay records and scene constants, and renders the original models with
simpler lighting, terrain, and effects. The game executable is never launched. Saves, Steam,
achievements, and personal settings are not used.

Generation requires **Python 3.10+**, a **.NET 8 SDK**, **FFmpeg**, and an OpenGL EGL driver
(including a software Mesa driver). Install media packages in a virtual environment:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r tools/requirements-media.txt
.venv/bin/python tools/generate_examples.py --game-dir /path/to/game
```

Use `--dotnet /path/to/dotnet` when the SDK is outside `PATH`. The first bridge build restores
Mono.Cecil 0.11.6 from NuGet. Subsequent generation reuses unchanged GIFs and local build artifacts.
`--output` selects a separate exported collection.

All examples with `show_image` or `show_output` enabled are attempted. Recordings use the source image dimensions,
camera, setup, timing, inventory, unlock exclusions, and seed. The simulation panel contains inventory
and output when enabled; the code remains searchable Markdown. GIFs loop at 15 fps, stop after
completion plus a one-second hold, and last at most 30 seconds including that hold. Sources with a negative seed get
an explicitly recorded effective seed.

Generated GIFs appear in collapsed **Animated example** disclosures. Every output-enabled example
also gets a collapsed **Example output** panel containing copyable interpreter text, including
expression results and tutorial diagnostics. Silent runs show *No output.* Text-only examples do
not render GIFs. Runs still executing at 30 seconds retain their GIF and captured text, with an
incomplete-output note; the generator lists capped examples by page, block, and GIF path for review.
The exported [extraction limits](../reference/gaps.md) page also lists GIFs still executing at the cap.

`example_media.json` records output text, completion status, coverage, failures, provenance,
effective seeds, and GIF checksums. English localization files are included in provenance so changes
to diagnostic messages invalidate cached output. The extraction manifest retains
all source configurations, setup, and code. Stale or missing GIFs are not embedded during text export.

`.media-cache/` contains local extracted assets, build artifacts, and adapted copies of game
assemblies. Never distribute that directory. Only GIFs and provenance belong in the exported
collection. The bridge replaces Unity resource loading, native math, and visual services, and turns
the simulator's UI wait into a frame boundary. Farming, world generation, and interpretation remain
in the game assemblies. Unknown engine dependencies are reported as gaps rather than simulated
with guessed behavior.

Run the dependency-free media regression checks with:

```sh
python tools/test_media.py
```

Set `TFWR_GAME_DIR` to the installation and `TFWR_DOTNET` to the SDK executable to additionally
run offline farming, mining, determinism, output, diagnostic, and loop-limit checks against a built
`.media-cache/bridge`. Use the virtual environment's Python to include the renderer check.
