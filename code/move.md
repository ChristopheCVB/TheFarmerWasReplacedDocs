[Documentation index](../README.md)

# `move`

`move(direction)`
Moves the drone into the specified `direction` by one tile.
If the drone moves over the edge of the farm it wraps back to the other side of the farm.

`East `  =  right
`West `  =  left
`North`  =  up
`South`  =  down

returns `True` if the drone has moved, `False` otherwise.

takes `200` ticks to execute if the drone has moved, `1` tick otherwise.

example:
`move(North)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_move`.
