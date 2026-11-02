[Documentation index](../README.md)

# `place`

`place(ground)`
Place blocks.

You can specify the block to be placed. Only blocks without special function can be placed. For example, you can `place(Grounds.Rock)` but not `place(Grounds.Clay)`.

returns `True` if the block was placed, `False` otherwise.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example:
`place(Grounds.Rock)`

Source: `EN/Strings/code_tooltips.txt`, `code_tooltip_place`.
