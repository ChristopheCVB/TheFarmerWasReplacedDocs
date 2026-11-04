[Documentation index](../../README.md)

[<- Functions](functions.md)

---

# Tuples

Tuples are a great way to combine multiple values into a single value.
To create a tuple, just separate the values with commas:

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
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
tuple = 1, 2
print(tuple)
```

<details>
<summary>Example output</summary>

<pre>(1,2)</pre>

</details>

You can also unpack them into several variables. In the code below, the tuple `(1, 2)` is unpacked into two variables, `a` and `b`.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
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
a, b = 1, 2
print(a)
a, b = b, a
print(a)
```

<details>
<summary>Example output</summary>

<pre>1
2</pre>

</details>

Tuples can be indexed like lists, but they are immutable and cannot be changed after creation.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
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
tuple = 1, 2
print(tuple[1])

tuple[0] = 3
```

<details>
<summary>Example output</summary>

<pre>2
Error: You can&#x27;t assign a tuple element because tuples are immutable.
In:&#32;
tuple[0] = 3
      ^^   &#32;
--------------------------------------------------------------------</pre>

</details>

Unlike lists, tuples can be used as keys in dictionaries.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
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
d = {(1,2):(4,5)}

print(d[(1,2)])
```

<details>
<summary>Example output</summary>

<pre>(4,5)</pre>

</details>

They can also be useful for returning multiple values in a function.

**Example conditions**

```json
{
  "execution_speed": 1,
  "digging_speed": 1,
  "action_ticks": 200,
  "operation_ticks": 100,
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
def f():
    return 1, 2

a, b = f()
```

<details>
<summary>Example output</summary>

*No output.*

</details>

---

[Lists](lists.md)      [Dictionaries](dicts.md)      [Functions](functions.md)

Source: `EN/docs/scripting/tuples.md`.
