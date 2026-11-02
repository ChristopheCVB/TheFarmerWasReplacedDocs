[Documentation index](../README.md)

# `range`

`range(start = 0, end, step = 1)`
Generates a sequence of numbers starting at `start`, ending right before reaching `end` (so `end` is excluded) using steps of size `step`.

Note that start is set to `0` by default, and if only one argument is given, it will bind to `end`. This isn't normally possible.
In Python, `range` is a class constructor that allows this strange behavior.

takes `1` tick to execute.

example:

```python
for i in range(10):
    print(i)

for i in range(2,6):
    print(i)

for i in range(10, 0, -1):
    print(i)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_range`.
