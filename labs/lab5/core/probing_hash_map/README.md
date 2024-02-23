# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/README.md))

### [Probing Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/probing_hash_map/README.md)
```shell
python labs probing_hash_map
```

For this third and final core exercise, we're going to again implement a hash map - but this time, using linear probing
rather than chaining.

`ProbingHashMap` contains much the same member variables as `ChainingHashMap`: a hash function, the length, the maximum
load factor, and an array, whose length the hashes must be less than, and which the hashes will be indices into.

However, the array's items are quite different. Instead of being `DoublyLinkedList[tuple[Key, Value]]`s, they're
`tuple[Key, Value] | EmptyCell`s. That is, they're either a key/value pair, or they're an empty cell.

We've defined a type `EmptyCell` to represent the two different states an empty cell can be in. In the lectures, these
are described as "empty" or "available". In these labs, we refer to them as "never used" or "now unused" repspectively.
(This is just to help you keep it clearer in your head what the distinction is while you're implementing the methods.)

The type `EmptyCell` is an "enum", short for "enumeration" or "enumerated type". All that means is that it's a type
whose values are one of some number of options. In this case, there are two: Anything of type `EmptyCell` is either
the value `EmptyCell.NEVER_USED` or the value `EmptyCell.NOW_UNUSED` - either one or the other, nothing else.

Another Python feature that you'll probably find useful for this exercise, which you may not have encountered before
is the `match` statement. Given an `item` from the array, you may want to write things like this:
```python
match item:
    case EmptyCell.NEVER_USED:
        do_something_if_an_empty_cell()
    case EmptyCell.NOW_UNUSED:
        do_something_if_an_available_cell()
    case key, value:
        do_something_if_a_mapping(key, value)
        do_something_with_the_key(key)
        do_something_with_the_value(value)
```

Depending on what `item` is, one of those three branches will run. Note that the cases can have multiple statements in
them, as shown in the third case above. Note also that you don't have to include all three branches, e.g. if you're
only interested in doing something if the `item` is a key/value pair, and are happy to do nothing otherwise, then you
can write:
```python
match item:
    case key, value:
        do_something_if_a_mapping(key, value)
```

In previous exercises, when we've been sure that the `item` is a pair, we've been able to destructure it like so to get
the key and the value:
```python
key, value = item
```

We can't necessarily do that here though, because the `item` might not be a pair, as it might instead be an `EmptyCell`.
Note that you can also combine cases, so if you want to do the same thing whether it's a true "empty cell" or is an
"available" cell, you can write:
```python
match item:
    case EmptyCell.NEVER_USED | EmptyCell.NOW_UNUSED:
        do_something_if_an_empty_or_available_cell()
```

Or, equivalently:
```python
match item:
    case EmptyCell():
        do_something_if_an_empty_or_available_cell()
```

Similarly, if you're only interested in if it's a pair, but not in binding names to the key and value, you can write:
```python
match item:
    case tuple():
        do_something_if_a_mapping()
```

Hopefully that helps. You can do it without `match` statements, e.g. just using `if` statements, but you'll probably
find that `match` makes your code much nicer.

Speaking of your code, you're again to implement the methods:
- `contains`
- `get`
- `insert`
- `remove`

Though the same methods, they are of course implemented quite differently to their counterparts in the previous
exercise. That said, there are some similarities, including that you'll need to call `_resize` in the same cases in the
`insert` and `remove` methods - i.e. to double the capacity if the load factor exceeds the maximum, or to halve it if
it drops below a quarter of the maximum.

As for how the methods are supposed to work, you're best served by downloading the lecture slides from Canvas and
referring to those. Do that, then crack open `exercise.py` and try to figure it out!
