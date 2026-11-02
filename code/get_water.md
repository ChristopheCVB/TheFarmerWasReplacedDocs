[Documentation index](../README.md)

# `get_water`

`get_water()` 
Get the current water level under the drone.

returns the water level under the drone as a number between `0` and `1`.

takes `1` tick to execute.

example:

```python
if get_water() < 0.5:
    use_item(Items.Water)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_get_water`.
