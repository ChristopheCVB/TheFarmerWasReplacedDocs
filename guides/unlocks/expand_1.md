[Documentation index](../../README.md)

[<- Speed Upgrade](speed.md)  | [Expand 2 ->](expand_2.md)
 | [Mining ->](mining.md)

---

# Expand 1

Your farm has grown! This space is not much use if you can't move the drone, so there is a new function `move()` that moves the drone. `move()` requires that you specify the direction in which you want the drone to move. There are four new constants for this: `North, East, South, West`

For example, `move(North)` will move the drone one square to the north.

If you move over the edge of the farm, the drone will wrap around to the other side.

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 1,
    "y": 3
  },
  "execution_speed": 2,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
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
while True:
	move(North)
```

---

[While Loop](../scripting/while.md)      [Operators](../scripting/operators.md)      [Expand 2](expand_2.md)

[move()](../../code/move.md)

Source: `EN/docs/unlocks/expand_1.md`.
