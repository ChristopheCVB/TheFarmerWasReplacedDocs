[Documentation index](../../README.md)

[<- While Loop](while.md)

---

# Break

`break` allows you to stop a loop early. When a `break` statement is reached, it immediately exits the innermost loop and starts running the code after that loop.

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
	break
print(i)
```

This prints `0` because `i` is `0` during the first iteration, after which the `break` statement ends the loop.

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
	if can_harvest():
		break
harvest()
```

This code runs the `while` loop until `can_harvest()` is `True`.
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
while not can_harvest():
	pass
harvest()
```

In nested loops, `break` always exits the innermost loop.

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
	for j in range(10):
		break
		print("this is never printed")
	print("this is printed 10 times")
```

---

[While Loop](while.md)      [For Loop](for.md)      [Continue](continue.md)

Source: `EN/docs/scripting/break.md`.
