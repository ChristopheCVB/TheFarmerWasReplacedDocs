[Documentation index](../../README.md)

[<- While Loop](../scripting/while.md)  | [Expand 1 ->](expand_1.md)
 | [Plant ->](plant.md)

---

# Speed Upgrade

The execution speed has doubled. The problem is that the drone now harvests faster than the grass can grow, resulting in no yield at all. To deal with this, [if](../scripting/if.md) branches and the [can_harvest()](../../code/can_harvest.md) function are now unlocked.

## Checking Before Harvesting

An `if` statement runs its code block once if the given condition is `True`.

The new function `can_harvest()` provides a useful condition. `can_harvest()` returns `True` if the plant under the drone can be harvested and `False` otherwise.

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

**Example setup**

```python
do_a_flip()
```

**Example code**

```python
if can_harvest():
	do_a_flip()
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/unlocks/speed-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

You can think of a return value like this as if the function call expression `can_harvest()` gets replaced by the returned value `True` during the evaluation of the `if`.

What happens when the above code runs:
- The `if` statement runs.
- `can_harvest()` is called.
- `can_harvest()` returns `True` because the grass is fully grown.
- The statement is now `if True:`.
- The branch executes because the value is `True`.

If the grass wasn't fully grown it would not do a flip.

Now we can use `if` to prevent the drone from harvesting too early.

---

[If](../scripting/if.md)      [While Loop](../scripting/while.md)

[harvest()](../../code/harvest.md)      [can_harvest()](../../code/can_harvest.md)

Source: `EN/docs/unlocks/speed.md`.
