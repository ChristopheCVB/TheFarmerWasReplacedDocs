[Documentation index](../README.md)

# `swap`

`swap(direction)`
Swaps the entity under the drone with the entity next to the drone in the specified `direction`.
Doesn't work on all entities.
Also works if one (or both) of the entities are `None`.

returns `True` if it succeeded, `False` otherwise.

takes `200` ticks to execute on success, `1` tick otherwise.

example:
`swap(North)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_swap`.
