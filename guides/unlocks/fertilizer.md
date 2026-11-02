[Documentation index](../../README.md)

[<- Watering](watering.md)  | [Mazes ->](mazes.md)

---

# Fertilizer

At some point, waiting for plants to grow is no longer efficient enough.
As with water, you will automatically receive 1 fertilizer every 10 seconds. The amount doubles with each upgrade.

Fertilizer can make plants grow instantly. `use_item(Items.Fertilizer)` reduces the remaining growing time of the plant under the drone by 2 seconds.

**Example conditions**

```json
{
  "items": [
    {
      "item": "fertilizer",
      "n": 10
    }
  ],
  "world_size": {
    "x": 1,
    "y": 1
  },
  "execution_speed": 2,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 1,
  "exclude_unlocks": [
    "watering"
  ],
  "starting_chunk": 0,
  "dlc_enabled": false
}
```

**Example code**

```python
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
```

This has some side effects.
Plants grown with fertilizer will be infected.

When a plant is infected, half of its yield is turned into `Items.Weird_Substance` when it is harvested.
Weird Substance can also be used on plants, which has the effect of toggling the infected status of the plant and all adjacent plants.

If you call `use_item(Items.Weird_Substance)` on an infected plant, it will cure it; if you use it on a healthy plant, it will infect it.

If you use it on an infected plant that has healthy neighbors, it will cure the plant but infect the neighbors and vice versa.

**Example conditions**

```json
{
  "items": [
    {
      "item": "weird_substance",
      "n": 10
    }
  ],
  "world_size": {
    "x": 3,
    "y": 3
  },
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 1,
  "exclude_unlocks": [
    "watering"
  ],
  "starting_chunk": 0,
  "dlc_enabled": false
}
```

**Example setup**

```python
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
```

**Example code**

```python
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
```

---

[Stats](../stats.md)      [Watering](watering.md)      [Mazes](mazes.md)

[use_item()](../../code/use_item.md)

Source: `EN/docs/unlocks/fertilizer.md`.
