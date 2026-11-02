[Documentation index](../../README.md)

[<- Speed Upgrade](../unlocks/speed.md)

---

# If

You can use `if`, `elif`, and `else` to run code conditionally.

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 1,
    "y": 1
  },
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
  "seed": 1,
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
condition1 = False
condition2 = False
condition3 = True

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
```

## Syntax

`if` statements allow you to run code only if a condition is `True`. They are like a `while` loop that doesn't loop.
An `if` statement takes a condition, just like a `while` loop, and executes its code block if the condition evaluates to `True`:

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 1,
    "y": 1
  },
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
  "seed": 1,
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
condition = True

if condition:
	do_a_flip()
```

You can also add an `else` block after the `if` block. The `else` block runs if the condition evaluates to `False`.

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 1,
    "y": 1
  },
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
  "seed": 1,
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
condition = False

if condition:
	do_a_flip()
else:
	harvest()
```

`elif` is short for "else if".

```python
if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c
```

can be shortened to:

```python
if condition1:
	#a
elif condition2:
	#b
else:
	#c
```

---

[While Loop](while.md)      [Operators](operators.md)      [Senses](../unlocks/senses.md)

Source: `EN/docs/scripting/if.md`.
