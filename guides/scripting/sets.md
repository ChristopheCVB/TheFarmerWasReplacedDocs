[Documentation index](../../README.md)

[<- Dictionaries](dicts.md)

---

# Sets

Sets are like [dictionaries](dicts.md), but without values. They're just an unordered set of keys. 

They are created like dictionaries, but without values.
`set = {North, East, West}`

Use `set()` to create an empty set. Note that `{}` creates an empty dictionary.

Use `set.add(elem)` to add a new element to the set.

Use `set.remove(elem)` to remove an element from a set.

Use `if elem in set:` to check if the set contains an element.

Use `for elem in set:` to iterate over all elements in the set.
For larger sets, the `in` operator is much faster than it would be on a list.

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
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North is in set")
else:
    print("North is not in set")
for element in my_set:
    print(element)
```

<details>
<summary>Example output</summary>

<pre>{}
{1,North}
{1}
North is not in set
1</pre>

</details>

Just like dictionaries, sets are unordered, so there are no guarantees about the order in which the elements are iterated.

Also, elements in sets are unique, so adding an element that is already in the set will not change the set.

---

[Dictionaries](dicts.md)      [Lists](lists.md)      [For Loop](for.md)

[len()](../../code/len.md)

Source: `EN/docs/scripting/sets.md`.
