# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Circular Dynamic Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/circular_dynamic_array_list/README.md)
```shell
python labs circular_dynamic_array_list
```

In this exercise, we're going to again extend our array list implementation with an extra member variable that improves
the efficiency of some operations.

In the previous exercise, `DynamicArrayList` generalised `StaticArrayList` by removing the constraint that the backing
array must always be full. It did this by adding a `_length` variable to keep track of how much of the array is being
used at any given moment, and this improved `insert_last` and `remove_last` from $\mathrm{O}(n)$ to amortized
$\mathrm{O}(1)$. (It also somewhat improved `insert_at` and `remove_at`, but less so.)

This time, `CircularDynamicArrayList` will generalise `DynamicArraylist` by relaxing the constraint that the first item
in the list must always be stored at the first index in the backing array. It will do this by adding a `_first_index`
variable for tracking the index within the array at the first item is stored. By doing this, `insert_first` and
`remove_first` will also improve from $\mathrm{O}(n)$ to amortized $\mathrm{O}(1)$. (And again, there will be a more
marginal improvement to `insert_at` and `remove_at`.)

Much of the basics of `CircularDynamicArrayList` are the same as `DynamicArrayList`, but there are some differences in
its implementation caused by this increased flexibility:

When e.g. `get`ting and `set`ting at a given index, that index into the list must first be converted to an index into
the array. This is done by offsetting and wrapping: The index is relative to `_first_index`, rather than `0`, but adding
that may result in an index past the end of the array, in which case you'll need to do a subtraction to have the indices
past that point restart from its beginning.

For example, if you have a list of 7 items, with the first being stored at index 4 in the array, and that array has
a capacity of 8, then a list index of 6 (the last index in a 7-item list) will convert to an array index of 2:
```
List:    4   5   6       0   1   2   3
Array:   0   1   2   3   4   5   6   7
       +---+---+---+---+---+---+---+---+
       | e | f | g |   | a | b | c | d |
       +---+---+---+---+---+---+---+---+
                         ^
                         |
                       first
```

Reallocating is much the same as in the previous exercise, the extra complexity being that you should reset
`_first_index` to `0` while you're at it, and thus, when copying items across, the indices in the old array won't
necessarily be the same as the indices in the new one.

The methods that you're tasked with implementing are:
- `resize`
- `get_first`
- `get_last`
- `get_at`
- `set_first`
- `set_last`
- `set_at`
- `insert_first`
- `insert_last`
- `insert_at`
- `remove_first`
- `remove_last`
- `remove_at`

If you worry that that seems a long list, bear in mind that all of the `*_first` and `*_last` methods can be implemented
in terms of their general `*_at` versions (e.g. `get_first()` can be implemented as `get_at(0)`).

_However_, the general `*_at` methods are more complex to implement, and therefore you may prefer to implement the
`*_first`/`*_last` as a sort of warm-up for them. If you just want to jump straight into the `*_at` methods though, you
can implement the `*_first`/`*_last` methods in terms of them, and thus implement only:
- `resize`
- `get_at`
- `set_at`
- `insert_at`
- `remove_at`

Which, I'm sure you'll agree, is a more appealing-looking length of list. Still, if you're struggling with them, perhaps
try implementing the simpler ones first.

Whichever approach you choose, good luck!

---

Next:
- [Linked Stacks](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/linked_stack/README.md)
