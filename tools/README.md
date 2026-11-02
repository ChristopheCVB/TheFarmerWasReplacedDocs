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
