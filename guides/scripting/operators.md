[Documentation index](../../README.md)

[<- Plant](../unlocks/plant.md)  | [Senses ->](../unlocks/senses.md)
 | [Variables ->](variables.md)

---

# Operators

Arithmetic operators: `+, -, *, /, //, %, **`
Comparison operators: `==, !=, <=, >=, <, >`
Boolean operators: `not, and, or`

Note: All numbers in the game are floating-point numbers, so all arithmetic operators are floating-point operators.
`//` is defined to floor the number after the division.

To use assignment operators, you need to unlock "Variables."

## Introduction

Operators allow you to compare, modify and combine values. 
The arithmetic operators `+, -, *, /, //, %, **` are used to perform common mathematical operations on numbers. 
The comparison operators `==, !=, <=, >=, <, >` are used to compare values. The result is always either `True` or `False`.
The logic operators (also called boolean operators) `not, and, or` are used to combine truth values.

## Arithmetic Operators

`+` and `-` are used for addition and subtraction.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2 + 3
```

<details>
<summary>Example output</summary>

<pre>5</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
3 - 2
```

<details>
<summary>Example output</summary>

<pre>1</pre>

</details>

`*`, `/` and `//` are used for multiplication and division.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2 * 3
```

<details>
<summary>Example output</summary>

<pre>6</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
5 / 2
```

<details>
<summary>Example output</summary>

<pre>2.5</pre>

</details>

`//` does the same thing as `/`, but the result is floored (rounded down to the nearest integer).

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
5 // 2
```

<details>
<summary>Example output</summary>

<pre>2</pre>

</details>

`%` is the modulo operator, also known as the remainder operator. It divides the two numbers and returns the remainder. You can also think of it as repeatedly subtracting the right-hand number from the left-hand number until the remainder is less than the right-hand number.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
4 % 2
```

<details>
<summary>Example output</summary>

<pre>0</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
5 % 2
```

<details>
<summary>Example output</summary>

<pre>1</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
6 % 2
```

<details>
<summary>Example output</summary>

<pre>0</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2 % 6
```

<details>
<summary>Example output</summary>

<pre>2</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
1.5 % 1
```

<details>
<summary>Example output</summary>

<pre>0.5</pre>

</details>

`**` is the power operator.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2**2
```

<details>
<summary>Example output</summary>

<pre>4</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
(-5)**3
```

<details>
<summary>Example output</summary>

<pre>-125</pre>

</details>

## Comparison Operators

`==` and `!=` check whether two values are equal (`==`) or not equal (`!=`). They can be used with all types of values.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2 == 2
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
Entities.Bush != Entities.Bush
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
3 != 3 + 1
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

`<=`, `>=`, `<`, and `>` can only be used with numbers. They check whether the left number is less than or equal to (`<=`), greater than or equal to (`>=`), less than (`<`), or greater than (`>`) the right number.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
1 <= 1
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
2 >= 3
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
-2 < -1
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
6 > 6
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

## Logic Operators

`not` simply inverts the value:

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
not False
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
not True
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

`and` evaluates to `True` only if both values are `True`.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
True and True
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
True and False
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
False and False
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

`or` evaluates to `True` if at least one of the values is `True`.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
True or True
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
True or False
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 1,
  "seed": 0,
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
False or False
```

<details>
<summary>Example output</summary>

<pre>False</pre>

</details>

Operators can be combined into larger expressions, but be careful about the order of operations. Use parentheses to make the intended order explicit.

**Example conditions**

```json
{
  "print_last_result": true,
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 200,
  "seed": 0,
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
(4 % 2 == 1 or 4 % 2 == 0) and 2 + 3 > 4
```

<details>
<summary>Example output</summary>

<pre>True</pre>

</details>

---

[Variables](variables.md)      [If](if.md)      [While Loop](while.md)      [Senses](../unlocks/senses.md)

Source: `EN/docs/scripting/operators.md`.
