[Documentation index](../README.md)

# `can_harvest`

`can_harvest()`
Used to find out if plants are fully grown.

returns `True` if there is an entity under the drone that is ready to be harvested, `False` otherwise.

takes `1` tick to execute.

example:

```python
if can_harvest():
    harvest()
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_can_harvest`.
