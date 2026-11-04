[Documentation index](../../README.md)

[<- First Program](../first_program.md)  | [Speed Upgrade ->](../unlocks/speed.md)

---

# While Loop

You have unlocked the `while` loop and the values `True` and `False`. The `while` loop keeps executing the loop body as long as the condition is `True`.

```python
while condition:
	#loop body
```

Don't worry about creating infinite loops. The drone might get stuck but won't freeze the whole game, you can just stop the running program and try again.

## For Beginners

Perhaps you have already tried to put several `harvest()` calls in a row:

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
  "operation_ticks": 200,
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
harvest()
harvest()
harvest()
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/scripting/while-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

This allows you to harvest several times in one program run.
However, it would be nice to harvest more than three times, and writing the same code multiple times quickly makes the program a mess.
The solution is a loop.
A loop allows you to run the same code multiple times.

The while loop takes a condition, which is a logical value that can only be in one of two states: `True` or `False`. 
Such a value is called a Boolean value.

The loop then executes the code inside the loop until the condition is False.
The while loop looks like this:

```python
while condition:
	#loop body
	#loop body
	#...
```

Where you have to replace "condition" with a boolean value and `#loop body` with whatever you want to do in the loop.

There are two constant boolean values available. Constants are values that never change during the program.

To create a constant Boolean value, simply write `True` or `False`.
So you could either write

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
  "operation_ticks": 200,
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
while False:
	do_a_flip()
```

<details>
<summary>Animated example</summary>

![Animated example 2](../../assets/examples/scripting/while-02.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

or

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
  "operation_ticks": 200,
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
while True:
	do_a_flip()
```

<details>
<summary>Animated example</summary>

![Animated example 3](../../assets/examples/scripting/while-03.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

The first will never perform a flip, and the second will perform flips forever (an infinite loop).

Normally, creating an infinite loop is a bad idea because it will freeze the program. In this game, however, there are delays between iterations, so the drone will keep performing flips until you stop it manually by pressing the Execute button again.

Notice how the line after the colon is indented. Indentation like this is used to separate blocks of code.
Just press Tab to add indentation and Shift + Tab (or Backspace) to remove it. If several lines are selected, Tab and Shift + Tab will apply to all of them.

Note: if you are playing the game through steam, pressing Shift + Tab will open the steam overlay instead. You can rebind the unindent shortcut in the game options, or the steam overlay shortcut in the steam overlay options.

Here, `do_a_flip()` and `pet_the_piggy()` are called repeatedly because they are inside the indented `while` block. However, `harvest()` never runs because it comes after that block.

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
  "operation_ticks": 200,
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
while True:
	do_a_flip()
	pet_the_piggy()
harvest()
```

<details>
<summary>Animated example</summary>

![Animated example 4](../../assets/examples/scripting/while-04.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 30 seconds.*

</details>

---

[For Loop](for.md)      [If](if.md)      [Break](break.md)      [Continue](continue.md)      [External Editor](../external_editor.md)

Source: `EN/docs/scripting/while.md`.
