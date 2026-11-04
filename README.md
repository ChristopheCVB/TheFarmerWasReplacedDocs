# The Farmer Was Replaced — English Documentation

Complete installed English guides and gameplay reference, including Underground/DLC content.

- [In-game documentation home](guides/home.md)
- [Getting started](guides/getting_started.md)
- [Code reference](code/index.md)
- [Unlocks and upgrades](unlocks/index.md)
- [Entities](objects/index.md)
- [Grounds](grounds/index.md)
- [Items](items/index.md)
- [Hats](hats/index.md)
- [Leaderboards](leaderboards/index.md)
- [Supplementary templates and labels](reference/templates.md)
- [Extraction limits and missing descriptions](reference/gaps.md)
- [Exporter maintenance and validation](tools/README.md)

## Coverage

65 guide pages; 91 code reference entries;
361 source text entries;
146 interactive examples converted to code and starting conditions;
76 offline example GIFs;
92 extracted example outputs;
183 packaged gameplay records; 5 extracted illustrations.

Packaged records: 26 grounds, 38 hats, 20 items, 30 leaderboards, 16 objects, 53 unlocks.

## Reading the reference

All unlock-gated content and hints are visible. Examples use the game's Python-like language.
Example conditions preserve gameplay configuration. Complete source examples, including visual
settings, are retained in the extraction manifest. Optional GIFs execute the game's interpreter
offline and render extracted models with simplified lighting and effects. Expand **Animated
example** beneath supported examples to view them. Clips show at most 30 seconds of execution.
Expand **Example output** for copyable interpreter output, expression results, and tutorial errors.
Silent examples show *No output.*; capped runs include a note that output may be incomplete.
Code and conditions remain available for all examples.
Media coverage and unsupported examples are recorded in `tools/example_media.json` when generated.

Reference tables contain stored base values, not unconditional promises about gameplay.
Upgrades, neighbors, depth, and controller logic can change actual values. Upgrade cost arrays
and factors are listed as stored; this export does not derive their runtime formula.
Source wording, including outdated entries and apparent mistakes, is preserved.
Templates retain literal source syntax inside fenced text blocks.

## Logical paths

`<game-data>/` means the game's persistent data directory. Its actual location depends
on the platform and launcher; it is a logical placeholder, not a literal filesystem path.

- `<game-data>/Saves/`: saves and in-game code files.
- `<game-data>/Backup/`: saved backups.
- `<game-data>/output.txt`: complete execution output.

## Sources

Source references are relative to the game installation. Unity version: `6000.0.43f1`.
The extraction manifest retains the UTC export timestamp, source hashes, and entry coverage.

Standalone UI labels, settings, error catalogs, news, audio, and unrelated artwork are excluded.
Live farm output and personal statistics require a running game; example output is captured offline.

## All guides

- [backup](guides/backup.md)
- [credits](guides/credits.md)
- [external editor](guides/external_editor.md)
- [first program](guides/first_program.md)
- [getting started](guides/getting_started.md)
- [home](guides/home.md)
- [output](guides/output.md)
- [break](guides/scripting/break.md)
- [comments](guides/scripting/comments.md)
- [continue](guides/scripting/continue.md)
- [debug](guides/scripting/debug.md)
- [dicts](guides/scripting/dicts.md)
- [for](guides/scripting/for.md)
- [functions](guides/scripting/functions.md)
- [if](guides/scripting/if.md)
- [import](guides/scripting/import.md)
- [lists](guides/scripting/lists.md)
- [operators](guides/scripting/operators.md)
- [scopes](guides/scripting/scopes.md)
- [sets](guides/scripting/sets.md)
- [tuples](guides/scripting/tuples.md)
- [variables](guides/scripting/variables.md)
- [while](guides/scripting/while.md)
- [stats](guides/stats.md)
- [auto unlock](guides/unlocks/auto_unlock.md)
- [bamboo](guides/unlocks/bamboo.md)
- [cactus](guides/unlocks/cactus.md)
- [carrots](guides/unlocks/carrots.md)
- [coal](guides/unlocks/coal.md)
- [costs](guides/unlocks/costs.md)
- [debug2](guides/unlocks/debug2.md)
- [debug place](guides/unlocks/debug_place.md)
- [dinosaurs](guides/unlocks/dinosaurs.md)
- [dynamite](guides/unlocks/dynamite.md)
- [expand 1](guides/unlocks/expand_1.md)
- [expand 2](guides/unlocks/expand_2.md)
- [explosive drill](guides/unlocks/explosive_drill.md)
- [fertilizer](guides/unlocks/fertilizer.md)
- [hats](guides/unlocks/hats.md)
- [iron](guides/unlocks/iron.md)
- [jump](guides/unlocks/jump.md)
- [leaderboard](guides/unlocks/leaderboard.md)
- [mazes](guides/unlocks/mazes.md)
- [megafarm](guides/unlocks/megafarm.md)
- [mining](guides/unlocks/mining.md)
- [mushroom](guides/unlocks/mushroom.md)
- [petrified pumpkins](guides/unlocks/petrified_pumpkins.md)
- [plant](guides/unlocks/plant.md)
- [polyculture](guides/unlocks/polyculture.md)
- [prospecting](guides/unlocks/prospecting.md)
- [pumpkins](guides/unlocks/pumpkins.md)
- [pyramid](guides/unlocks/pyramid.md)
- [quartz](guides/unlocks/quartz.md)
- [rice](guides/unlocks/rice.md)
- [senses](guides/unlocks/senses.md)
- [simulation](guides/unlocks/simulation.md)
- [special soils](guides/unlocks/special_soils.md)
- [speed](guides/unlocks/speed.md)
- [sunflowers](guides/unlocks/sunflowers.md)
- [timing](guides/unlocks/timing.md)
- [treasure map](guides/unlocks/treasure_map.md)
- [trees](guides/unlocks/trees.md)
- [underground leaderboard](guides/unlocks/underground_leaderboard.md)
- [underground senses](guides/unlocks/underground_senses.md)
- [watering](guides/unlocks/watering.md)
