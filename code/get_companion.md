[Documentation index](../README.md)

# `get_companion`

`get_companion()` 
Get the preferred companion of the plant under the drone.

returns a tuple of the form `(companion_type, (companion_x_position, companion_y_position))`

takes `1` tick to execute.

example:

```python
companion = get_companion()
if companion != None:
    plant_type, (x, y) = companion
    print("Companion:", plant_type, "at", x, ",", y)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_get_companion`.
