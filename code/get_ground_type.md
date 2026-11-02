[Documentation index](../README.md)

# `get_ground_type`

`get_ground_type(direction = None)`
Find out what kind of ground is under the drone.

If `direction` is not `None` it checks the neighboring tile in the given direction instead.

returns the type of the ground on the checked tile.

takes `1` tick to execute.

example:

```python
if get_ground_type() != Grounds.Soil:
    till()
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_get_ground_type`.
