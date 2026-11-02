[Documentation index](../README.md)

# `use_item`

`use_item(item, n=1)` 
Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer`.

returns `True` if an item was used, `False` otherwise.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example:
`use_item(Items.Fertilizer)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_use_item`.
