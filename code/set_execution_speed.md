[Documentation index](../README.md)

# `set_execution_speed`

`set_execution_speed(speed)`
Limits the speed at which the program is executed to better see what's happening.

A `speed` of `1` is the speed the drone has without any speed upgrades.
A `speed` of `8` makes the code execute `8` times faster and corresponds to the speed of the drone after `3` speed upgrades.
A `speed` of `0.5` makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

If `speed` is faster than the execution can currently go it will just go at max speed.

If `speed` is `0` or negative, the speed is changed back to max speed.
The effect will also stop when the execution stops.

returns `None`

takes `200` ticks to execute.

example:
`set_execution_speed(1)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_set_execution_speed`.
