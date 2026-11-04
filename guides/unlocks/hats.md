[Documentation index](../../README.md)

[<- While Loop](../scripting/while.md)

---

# Hats

You have unlocked a few new hat colors for your drone.

Equip them like this:

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
change_hat(Hats.Gray_Hat)
do_a_flip()
change_hat(Hats.Purple_Hat)
do_a_flip()
change_hat(Hats.Green_Hat)
do_a_flip()
change_hat(Hats.Brown_Hat)
do_a_flip()
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/hats-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

---

[Dinosaurs](dinosaurs.md)      [First Program](../first_program.md)

[change_hat()](../../code/change_hat.md)

Source: `EN/docs/unlocks/hats.md`.
