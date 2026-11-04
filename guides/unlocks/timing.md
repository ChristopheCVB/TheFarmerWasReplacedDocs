[Documentation index](../../README.md)

[<- Debug](../scripting/debug.md)  | [Simulation ->](simulation.md)

---

# Timing

If you really want to optimize your methods, you need to understand how time is measured in this game. This unlock is all about that.

## New Functions

There are two useful functions to measure how long things take:

`get_time()` returns the time in seconds since the start of the game.

`get_tick_count()` returns the number of ticks performed since the start of execution.

These two functions, as well as `quick_print()`, are completely free. Even the call operation is free for them.

**Example conditions**

```json
{
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
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
```

<details>
<summary>Example output</summary>

<pre>0.5 201</pre>

</details>

## Runtime Details

### Heads-Up

This is not how performance works in the real world. These are just rules made up for this game to have a consistent and understandable timing model.
You will probably only care about this if you want to hyper-optimize your code.

The basic unit of time for code execution is called a "tick." Without speed upgrades and power, execution proceeds at a rate of `400` ticks per second.

In general, operations that combine two values such as `+, -, *, /, //, %, and, or, ...` take one tick to run.
Unary `-` and `not` are free.
An `if` branch also takes one tick to run (in addition to the time it takes to evaluate the condition expression).
Function calls and variable reads and writes are free but function definitions take 1 tick.
`import` statements are free.
Accessing an imported module with the `.` operator is free.
If a function or module has been passed via arguments or variable assignments, using it will cost 1 tick instead of 0.
`for` and `while` loops take one tick to start, but the iterations are free (not counting the time to evaluate the condition/sequence expressions).
`return`, `break` and `continue` are all free.
`pass` takes one tick, so it can be used to create precise delays.
Indexing into a data structure takes one tick for the index operator and, in the case of a dictionary or set, additional ticks depending on the size of the key.

The number of ticks that built-in functions take to execute is documented on each function's page.

---

[Debug](../scripting/debug.md)      [Simulation](simulation.md)      [Leaderboard](leaderboard.md)

[get_time()](../../code/get_time.md)      [get_tick_count()](../../code/get_tick_count.md)      [quick_print()](../../code/quick_print.md)

Source: `EN/docs/unlocks/timing.md`.
