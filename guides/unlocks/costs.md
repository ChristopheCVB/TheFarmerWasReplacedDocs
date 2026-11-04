[Documentation index](../../README.md)

[<- Dictionaries](../scripting/dicts.md)  | [Auto Unlocks ->](auto_unlock.md)

---

# Costs

Any cost can be represented as a dictionary that maps items to numbers.

The `get_cost()` function returns such a dictionary. It returns the cost of a plant or an unlock.

**Example conditions**

```json
{
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
print(get_cost(Entities.Pumpkin))
```

<details>
<summary>Example output</summary>

<pre>{Items.Carrot:1}</pre>

</details>

For unlocks, you can pass an optional second argument specifying the unlock level whose cost you want. By default, it uses the current unlock level.

**Example conditions**

```json
{
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
print(get_cost(Unlocks.Loops, 0))
print(get_cost(Unlocks.Loops, 1))
```

<details>
<summary>Example output</summary>

<pre>{Items.Hay:5}
{}</pre>

</details>

For unlocks that are already at the maximum level, `get_cost()` returns an empty dictionary.

**Example conditions**

```json
{
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
cost = get_cost(Entities.Carrot)
for item in cost:
	if num_items(item) < cost[item]:
		print("missing", cost[item] - num_items(item), item)
```

<details>
<summary>Example output</summary>

<pre>missing 1 Items.Hay
missing 1 Items.Wood</pre>

</details>

---

[Dictionaries](../scripting/dicts.md)      [Auto Unlocks](auto_unlock.md)      [Leaderboard](leaderboard.md)

[get_cost()](../../code/get_cost.md)

Source: `EN/docs/unlocks/costs.md`.
