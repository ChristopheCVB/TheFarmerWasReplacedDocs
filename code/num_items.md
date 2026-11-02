[Documentation index](../README.md)

# `num_items`

`num_items(item)` 
Find out how much of `item` you currently have.

returns the number of `item` currently in your inventory.

takes `1` tick to execute.

example:

```python
if num_items(Items.Fertilizer) > 0:
    use_item(Items.Fertilizer)
```

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_num_items`.
