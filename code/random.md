[Documentation index](../README.md)

# `random`

`random()`
Samples a random number between 0 (inclusive) and 1 (exclusive).

returns the random number.

takes `1` ticks to execute.

example:

```python
def random_elem(list):
	index = random() * len(list) // 1
	return list[index]
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_random`.
