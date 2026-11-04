[Documentation index](../../README.md)

[<- Operators](operators.md)  | [Lists ->](lists.md)
 | [Functions ->](functions.md)

---

# Variables

Variables can be thought of as named containers that can hold a value.
The `=` operator is used to declare a variable and store a value in it.

`variable_name = value`

The left-hand side of the operator is the variable name. You can give it any valid name you want.
The right-hand side is an expression whose resulting value will be stored in the variable.

Declare a variable named `a` and store the value `5` in it:
`a = 5`
Declare a variable named `b` and store the return value of `can_harvest()` in it:
`b = can_harvest()`

Do not confuse the `=` operator with the `==` operator. 
The `==` operator checks whether two values are equal and returns `True` or `False`.
The `=` operator assigns the value on the right to the name on the left.

After a variable has been assigned, you can use it in the code to retrieve the value it contains.

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

**Example code**

```python
a = 5
for i in range(a):
	do_a_flip()
```

<details>
<summary>Animated example</summary>

![Animated example 1](../../assets/examples/scripting/variables-01.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 15 seconds.*

</details>

The above loop is executed 5 times because `a` is set to `5`.
The `i` in the `for` loop is also a variable. During each iteration, it is automatically assigned the current value from the sequence. It doesn't have to be called `i`; you can give it any valid variable name.

Variables also let you do the same thing with a while loop:

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

**Example code**

```python
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
```

<details>
<summary>Animated example</summary>

![Animated example 2](../../assets/examples/scripting/variables-02.gif)

*Offline recreation using extracted game models; simplified visuals. Clips are limited to 15 seconds.*

</details>

This does the same thing as the `for` loop above, but we have to increment `i` manually.
To increment `i`, we set it to its current value plus `1`. Changing a variable based on its previous value is very common.
It can be abbreviated using these operators: `+=, -=, *=, /=, %=`

`i = i + 1` is the same as `i += 1`
`a = a / 3` is the same as `a /= 3`

---

[Operators](operators.md)      [While Loop](while.md)      [For Loop](for.md)      [Functions](functions.md)      [Name Scopes](scopes.md)

Source: `EN/docs/scripting/variables.md`.
