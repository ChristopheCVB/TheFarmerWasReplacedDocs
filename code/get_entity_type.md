[Documentation index](../README.md)

# `get_entity_type`

`get_entity_type(direction = None)`
Find out what kind of entity is under the drone.

If `direction` is not `None` it checks the neighboring tile in the given direction instead.

returns `None` if the checked tile is empty, otherwise returns the type of the entity on that tile.

takes `1` tick to execute.

example:

```python
if get_entity_type() == Entities.Grass:
    harvest()
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_get_entity_type`.
