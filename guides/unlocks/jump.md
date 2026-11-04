[Documentation index](../../README.md)

[<- Coal](coal.md)

---

# Jumping

Your drone has unlocked the `jump()` command. You use it by passing it an unlock as an argument, such as `Unlocks.Iron`.

This command allows you to target certain resources that are hidden in the ground and instantly jump down to them. It is especially useful for debugging or skipping to an ore vein that you have recently missed.

After jumping, the target resource should be within 3 blocks of the top block surface. `jump()` can only be used once per program execution, further jump attempts will produce an error.

The following example jumps down to [rice](rice.md), finds the clay layer and plants a row of rice terraces:

**Example conditions**

```json
{
  "items": [
    {
      "item": "hay",
      "n": 10
    }
  ],
  "world_size": {
    "x": 4,
    "y": 4
  },
  "execution_speed": 1,
  "digging_speed": 4,
  "action_ticks": 200,
  "operation_ticks": 20,
  "seed": 1,
  "exclude_unlocks": [
    "watering",
    "fertilizer",
    "mushrooms"
  ],
  "starting_chunk": 0
}
```

**Example code**

```python
# Jump close to the rice resource
jump(Unlocks.Rice)

# Plant a row of rice terraces
for i in range(get_world_size()):
    # Jump is not exact, dig away the last blocks
    while get_ground_type() != Grounds.Clay:
        dig()

    plant(Entities.Rice)

    move(East)
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/jump-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 15 seconds.*

</details>

## Compatible Unlocks

`jump()` only works with the following mining unlocks:
- Coal
- Iron
- Quartz
- Rice
- Petrified_Pumpkins
- Special_Soils
- Pyramid
- Treasure_Map
- Mushrooms
- Dynamite

---

[jump()](../../code/jump.md)

Source: `EN/docs/unlocks/jump.md`.
