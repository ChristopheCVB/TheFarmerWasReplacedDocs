[Documentation index](../README.md)

# `plant`

`plant(entity)` 
Spends the cost of the specified `entity` and plants it under the drone.
It fails if you can't afford the plant, the ground type is wrong or there's already a plant there.

returns `True` if it succeeded, `False` otherwise.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example:
`plant(Entities.Bush)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_plant`.
