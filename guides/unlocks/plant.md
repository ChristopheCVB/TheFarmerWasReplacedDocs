[Documentation index](../../README.md)

[<- Speed Upgrade](speed.md)  | [Carrots ->](carrots.md)
 | [Debug ->](../scripting/debug.md)
 | [Operators ->](../scripting/operators.md)

---

# Plant

Grass is nice because it grows automatically. All other plants have to be planted with the `plant()` function. The only plant you can plant right now is a bush.
You can pass the type of plant you want to plant to the function like this:

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
plant(Entities.Bush)
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/plant-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 15 seconds.*

</details>

This will plant a bush under the drone.

Call `clear()` to reset the farm to all grass and reset the drone position.

It seems that if you grow more than one type of plant on the farm at the same time, you can sometimes get a higher yield. You'll need to research polyculture to learn more.

---

[Stats](../stats.md)      [If](../scripting/if.md)      [Senses](senses.md)      [Polyculture](polyculture.md)

[harvest()](../../code/harvest.md)      [plant()](../../code/plant.md)

Source: `EN/docs/unlocks/plant.md`.
