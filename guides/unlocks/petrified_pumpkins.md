[Documentation index](../../README.md)

[<- Rice](rice.md)

---

# Petrified Pumpkins

Apparently you can find pumpkins underground. They have turned solid and become petrified, but are still good enough for our purposes. You can `dig()` them to obtain pumpkins.

This provides an alternative way to obtain pumpkins without farming them above ground. If you prefer farming, you can safely ignore petrified pumpkins altogether.

**Example conditions**

```json
{
  "items": [],
  "exclude_unlocks": [
    "mushrooms",
    "watering",
    "fertilizer",
    "pyramid",
    "dynamite",
    "quartz"
  ],
  "world_size": {
    "x": 6,
    "y": 6
  },
  "execution_speed": 8,
  "digging_speed": 16,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 3
}
```

**Example setup**

```python
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
```

**Example code**

```python
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z - 2 and get_ground_type() != Grounds.Petrified_Pumpkin:
            dig()
        move(North)
    move(East)
for _ in range(3):
    dig()
    move(East)
    dig()
    move(South)
    dig()
    move(West)
    dig()
    move(West)
    dig()
    move(North)
    dig()
    move(North)
    dig()
    move(East)
    dig()
    move(East)
    dig()
    move(South)
    move(West)
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/petrified_pumpkins-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 15 seconds.*

</details>

Petrified pumpkins occur underground in blocks of 3x3x3 or 5x5x5. There is no surefire way to find them, so you just have to hope your drone digs into one, but they occur in the hard dirt under the stone-and-iron layer, about the same height as quartz (if you have it unlocked).

---

[Stats](../stats.md)      [Mining](mining.md)      [Underground Senses](underground_senses.md)

[move()](../../code/move.md)      [dig()](../../code/dig.md)      [get_ground_type()](../../code/get_ground_type.md)

Source: `EN/docs/unlocks/petrified_pumpkins.md`.
