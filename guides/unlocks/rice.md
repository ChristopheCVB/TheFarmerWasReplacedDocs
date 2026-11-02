[Documentation index](../../README.md)

[<- Mining](mining.md)  | [Bamboo ->](bamboo.md)
 | [Petrified Pumpkins ->](petrified_pumpkins.md)
 | [Perlite and Loam ->](special_soils.md)

---

# Rice

Below the surface and the `Grounds.Dirt` layer you will find a thin sheet of `Grounds.Clay`. As it turns out, this fertile and soaked ground is perfect for planting rice seedlings.

You might find the following code useful to dig down until you find clay and plant rice:

**Example conditions**

```json
{
  "items": [],
  "exclude_unlocks": [
    "watering",
    "fertilizer"
  ],
  "world_size": {
    "x": 4,
    "y": 4
  },
  "execution_speed": 8,
  "digging_speed": 4,
  "action_ticks": 200,
  "operation_ticks": 200,
  "seed": 1
}
```

**Example setup**

```python
move(East)
```

**Example code**

```python
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
```

As long as your drone is above a `Grounds.Clay` block, you can use `plant(Entities.Rice)` to plant rice seedlings into the clay, then `can_harvest()` to check if the rice has fully grown, and finally `harvest()` to gain rice.

## Terraces

Once you plant rice, the ground will turn into `Grounds.Rice_Terrace` to provide the perfect environment for the rice to mature. Once the rice is fully grown, the ground will dry out and turn into `Grounds.Dry_Rice_Terrace` and cannot be used to plant more rice. Luckily, the sheet is a few blocks thick, so you can `dig()` the block away and plant new rice on the `Grounds.Clay` below. And, if the sheet runs out, you can always just `clear()` the world and dig down to a fresh sheet.

---

[Stats](../stats.md)      [Mining](mining.md)      [Underground Senses](underground_senses.md)      [If](../scripting/if.md)      [For Loop](../scripting/for.md)

[harvest()](../../code/harvest.md)      [plant()](../../code/plant.md)      [move()](../../code/move.md)      [dig()](../../code/dig.md)      [get_ground_type()](../../code/get_ground_type.md)

Source: `EN/docs/unlocks/rice.md`.
