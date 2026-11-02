[Documentation index](../../README.md)

[<- Plant](plant.md)  | [Watering ->](watering.md)
 | [Trees ->](trees.md)

---

# Carrots

Before you can plant carrots with `plant(Entities.Carrot)`, you have to till the soil. This will change the ground to `Grounds.Soil`. To till the soil, simply call `till()`. Calling `till()` again will change it back to `Grounds.Grassland`.

Planting carrots costs wood and hay. These items will be automatically removed when calling `plant(Entities.Carrot)`.

**Example conditions**

```json
{
  "items": [
    {
      "item": "hay",
      "n": 1
    },
    {
      "item": "wood",
      "n": 1
    }
  ],
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
till()
plant(Entities.Carrot)
for _ in range(8):
    do_a_flip()
harvest()
till()
```

You can see the cost of any plant on its [own page](../../objects/carrot.md).

---

[Stats](../stats.md)      [Plant](plant.md)      [Watering](watering.md)      [If](../scripting/if.md)      [Senses](senses.md)      [Polyculture](polyculture.md)

[harvest()](../../code/harvest.md)      [plant()](../../code/plant.md)      [move()](../../code/move.md)      [till()](../../code/till.md)

Source: `EN/docs/unlocks/carrots.md`.
