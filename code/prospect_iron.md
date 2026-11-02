[Documentation index](../README.md)

# `prospect_iron`

`prospect_iron()`
Uses coal to look for iron.

returns the direction to the nearest iron ore (`North`, `East`, `South`, or `West`) if one is nearby. Returns `None` if no iron is nearby, or if you don't have enough coal, or if the drone is already above a piece of iron.

costs 1 coal to execute.

takes `1` tick to execute.

example:

```python
while prospect_iron() != None:
    move(prospect_iron())
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_prospect_iron`.
