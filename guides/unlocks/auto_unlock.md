[Documentation index](../../README.md)

[<- Costs](costs.md)

---

# Auto Unlocks

To fully automate the game, you can use the `unlock()` function to automatically unlock features.
For example, you can use `unlock(Unlocks.Speed)` and `unlock(Unlocks.Expand)` to unlock the speed and expansion features.

**Example conditions**

```json
{
  "items": [
    {
      "item": "hay",
      "n": 300
    },
    {
      "item": "wood",
      "n": 100000
    }
  ],
  "world_size": {
    "x": 1,
    "y": 1
  },
  "execution_speed": 1,
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
for _ in range(6):
    harvest()
    unlock(Unlocks.Grass)
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/auto_unlock-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

To determine the cost of an unlock, simply use the `get_cost()` function as you would for a plant or item.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 200,
  "seed": 1,
  "exclude_unlocks": [
    "watering",
    "fertilizer",
    "loops"
  ],
  "starting_chunk": 0,
  "dlc_enabled": false
}
```

**Example code**

```python
print(get_cost(Unlocks.Loops))
```

<details>
<summary>Example output</summary>

<pre>{Items.Hay:5}</pre>

</details>

---

[Costs](costs.md)      [Dictionaries](../scripting/dicts.md)      [If](../scripting/if.md)      [Leaderboard](leaderboard.md)

[get_cost()](../../code/get_cost.md)      [unlock()](../../code/unlock.md)

Source: `EN/docs/unlocks/auto_unlock.md`.
