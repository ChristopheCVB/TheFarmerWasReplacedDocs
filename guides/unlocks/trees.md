[Documentation index](../../README.md)

[<- Carrots](carrots.md)  | [Pumpkins ->](pumpkins.md)

---

# Trees

[Trees](../../objects/tree.md) are a better way to get wood than bushes. They give 5 wood each. Like bushes, they can be planted on grass or soil.

Trees like to have some space and planting them right next to each other will slow down their growth. The growing time is doubled for each tree that is on a tile directly to the north, east, west or south of it. So if you plant trees on every tile, they will take `2*2*2*2 = 16` times longer to grow.

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 3,
    "y": 3
  },
  "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/trees-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

**Show**

 
The `%` operator can be useful here. The `%` operator returns the remainder of the division. Even numbers divided by `2` have a remainder of `0` and odd numbers divided by `2` have a remainder of `1`.
So you can check if a number is even like this:

**Example conditions**

```json
{
  "items": [],
  "world_size": {
    "x": 2,
    "y": 1
  },
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 200,
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
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
```

<details>
<summary>Example output</summary>

<pre>is_even(0):  True
is_even(1):  False
is_even(2):  True
is_even(5):  False
is_even(-1):  False
is_even(x):  True</pre>

</details>

---

[Stats](../stats.md)      [Operators](../scripting/operators.md)      [If](../scripting/if.md)      [For Loop](../scripting/for.md)      [Polyculture](polyculture.md)

[harvest()](../../code/harvest.md)      [plant()](../../code/plant.md)      [move()](../../code/move.md)

Source: `EN/docs/unlocks/trees.md`.
