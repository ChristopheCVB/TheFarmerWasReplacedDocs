[Documentation index](../../README.md)

[<- First Program](../first_program.md)

---

# Comments

Comments are parts of the code that are ignored during execution.
Comments can be added using `#`. Anything on the same line after the `#` is a comment and will be ignored.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
  "seed": 0,
  "exclude_unlocks": [
    "watering",
    "fertilizer"
  ],
  "starting_chunk": 0,
  "dlc_enabled": false
}
```

**Example code**

```python
#this is a comment
#harvest()
```

This can be useful for adding notes to the code or temporarily disabling parts of it without deleting them.

A comment on the line before a function definition becomes part of the information that appears when you hover over the function name.

---

[First Program](../first_program.md)      [Debug](debug.md)      [Functions](functions.md)

Source: `EN/docs/scripting/comments.md`.
