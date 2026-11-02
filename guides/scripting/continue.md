[Documentation index](../../README.md)

[<- While Loop](while.md)

---

# Continue

`continue` stops the current iteration of a loop and jumps to the next iteration of the innermost loop.

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
for i in range(10):
	print("this happens every time")
	continue
	print("this is never printed")
```

This runs all `10` iterations of the loop, but the `print` statement after the `continue` is always skipped.

It also works on `while` loops.

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

**Example setup**

```python
plant(Entities.Tree)
```

**Example code**

```python
while True:
	if not can_harvest():
		continue

	harvest()
```

This code calls `harvest()` only when `can_harvest()` is `True`.
It has the same effect as:

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

**Example setup**

```python
plant(Entities.Tree)
```

**Example code**

```python
while True:
	if can_harvest():
		harvest()
```

In nested loops, `continue` always affects the innermost loop.

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
for i in range(2):
	for j in range(2):
		print("this is printed 4 times")
		continue
		print("this is never printed")
	print("this is printed 2 times")
```

---

[While Loop](while.md)      [For Loop](for.md)      [Break](break.md)

Source: `EN/docs/scripting/continue.md`.
