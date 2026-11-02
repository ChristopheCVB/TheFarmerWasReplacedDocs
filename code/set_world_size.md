[Documentation index](../README.md)

# `set_world_size`

`set_world_size(size)`
Limits the size of the farm to better see what's happening.
Sets the farm to a `size` x `size` grid.
The smallest `size` possible is `3`.
A `size` smaller than `3` will change the grid back to its full size.
The effect will also stop when the execution stops.
It also clears the farm and resets the drone's position, but only if the size has actually changed.

returns `None`

takes `200` ticks to execute.

example:
`set_world_size(5)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_set_world_size`.
