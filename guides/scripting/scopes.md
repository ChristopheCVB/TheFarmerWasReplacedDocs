[Documentation index](../../README.md)

[<- Functions](functions.md)

---

# Name Scopes

Scopes determine where variables can be accessed. A scope is essentially a mapping from names to values.
They work much as they do in Python.

There is a global scope, and each function has a local scope.
When you define a variable, it gets added to the current scope.
Anything outside of a function definition is considered part of the global scope.

`x = 1`
Assigns a value of `1` to the name `x` in the global scope.

This `def` statement assigns a function to the name `f` in the global scope.

```python
def f():
    
```
Assigns a value of `1` to the name `y` in the local scope of `f`.
```python
    y = 1

    
```
Assigns a function to the name `g` in the local scope of `f`.
```python
    def g():
        pass
```

`f()`
Retrieves the function stored in `f` from the global scope and calls it.

`print(y)`
This `print` statement in the global scope throws an error because `y` was never declared in the global scope, so we can't read it here.
It only existed in the local scope of `f`.

## The global Keyword

By default, all variables in functions bind to the local scope, even if a variable with the same name exists in the global scope.

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
x = 0

def f():
    x = 1
f()
print(x)
```

This code prints `0` because the local `x` inside `f` is not the same variable as the global `x`, so the global `x` remains unchanged. This is important because otherwise a function call could accidentally overwrite a global variable that happens to have the same name as one of the function's local variables.

If you want to write to a global variable, you must do so explicitly using the `global` keyword.

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
x = 0

def f():
    global x
    x = 1
f()
print(x)
```

In this example, `global x` binds `x` to the global variable `x` defined above it. The code will now print `1`.
Note that changing global variables is usually the first step towards spaghetti code, where every part of the program affects every other part of the program, so don't overuse it.

## Loops and Branches

Loops and branches do not create their own scopes, so anything declared within them can still be used outside.

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
for i in range(3):
    pass
print(i)
```

This prints `2` because the last iteration of the `for` loop assigned `2` to `i`.

---

[Variables](variables.md)      [Functions](functions.md)      [Import](import.md)      [Mega Farm](../unlocks/megafarm.md)

Source: `EN/docs/scripting/scopes.md`.
