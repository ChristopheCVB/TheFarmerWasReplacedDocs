[Documentation index](../../README.md)

[<- Variables](variables.md)  | [Dictionaries ->](dicts.md)

---

# Lists

Lists are an easy way to store multiple values in a single variable.
You can create new lists like this:

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
some_list = [2, True, Items.Hay]
print(some_list)
```

The list now contains the values `2`, `True`, and `Items.Hay`.
A list can also be empty:

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
empty_list = []
print(empty_list)
```

You can access an element of a list by its index. The index is `0` for the first element, `1` for the second element, `2` for the third, and so on.

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

**Example setup**

```python
till()
```

**Example code**

```python
entities = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(entities[1])
```

You can iterate over a list using a `for` loop. The following example adds up all the elements in the list.

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
numbers = [4, 7, 2, 5]
sum = 0
for number in numbers:
	sum += number
print(sum)
```

The following list methods allow you to add and remove elements:

`elements.append(elem)` adds an element to the end of the list:

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
numbers = [2, 6, 12]
numbers.append(7)
print(numbers)
```

`elements.remove(elem)` removes the first occurrence of an element from a list:

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
numbers = [1, 2, 4, 2]
numbers.remove(2)
print(numbers)
```

`elements.insert(index, elem)` inserts an element at the given index:

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
some_list = [Entities.Tree, Items.Hay]
some_list.insert(1, Items.Wood)
print(some_list)
```

`elements.pop(index)` removes the element at the specified index.
If no index is specified, the last item is removed.

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
numbers = [3, 5, 8, 25]
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
```

The `len()` function returns the length of the list.

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
numbers = [3, 5, 8, 25]
print(len(numbers))
```

Lists have reference semantics. This means that assigning a list to a variable assigns the same list object to that variable, rather than making a copy of the list.
If two variables reference the same list, changes to the list will be seen by both.

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
a = [1, 2]
b = a
b.pop()
print(a)
print(b)
```

---

[Variables](variables.md)      [For Loop](for.md)      [Tuples](tuples.md)      [Dictionaries](dicts.md)      [Sets](sets.md)

[len()](../../code/len.md)

Source: `EN/docs/scripting/lists.md`.
