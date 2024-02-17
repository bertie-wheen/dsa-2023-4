# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Unsorted Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/unsorted_array_map/README.md)
```shell
python labs unsorted_array_map
```

This exercise is the first of three different map types we'll implement in these labs.

We define the map interface to be:
```python
build           (items: Iterator[tuple[Key, Value]]) -> Map[Key, Value]
contains        (self, key: Key)                     -> bool
is_empty        (self)                               -> bool
get_length      (self)                               -> int
get             (self, key: Key)                     -> Value                       ! KeyError
insert          (self, key: Key, new_value: Value)   -> None
remove          (self, key: Key)                     -> Value                       ! KeyError
iterator        (self)                               -> Iterator[tuple[Key, Value]]
keys_iterator   (self)                               -> Iterator[Key]
values_iterator (self)                               -> Iterator[Value]
```

As with the list interface we defined in lab 2, the `Map[Key, Value]` return type of `build` stands for whatever the
specific map type we're implementing is, and the `! KeyError` notation represents that `get` and `remove` may raise
`KeyError`s.

The lectures define it to be:
```
build(X)
.len()
.find(k)
.insert(x)
.remove(k)
```

There are a few differences, but they're not major. There are a couple of renamings - `get_length` from `len`, and
`get` from `find` - and some operations which we additionally include here, but are somewhat secondary and not
necessarily part of a minimal interface - `contains` and `is_empty`, which work similarly to their list counterparts,
and `iterator`, `keys_iterator` and `values_iterator`.

Regarding the iterator methods, they're not so different to those we've met before. You use `iterator` to iterate over
the items in the collection - but in a map, the items are key/value mappings, and we choose to represent these as pairs
of a key and a value. This is not the only way to do it - for example, there are advantages to defining a type such as
`MapEntry[Key, Value]`, though we don't do that here in order to simplify the presentation. (Incidentally, "entries" is
a common term you'll encounter when talking about the items, i.e. the key/value mappings, in a map.) The lectures take
another approach again, which is that items aren't exactly key/value mappings, as such, but are rather items with the
constraint that they have some intrinsically associated `key`. (This sort of approach is particularly well-suited to
when the types of items you're working with - perhaps `User`s or `Product`s - have an associated `id`.)

The `keys_iterator` and `values_iterator` methods might seem theoretically unnecessary, but many maps you'll encounter
in your programming will have (equivalents of) them, as they turn out to be very often useful in practice.

For purposes of this exercise, though, you needn't concern yourself with them, as the only methods you're asked to
implement are:
- `insert`
- `remove`

These - as you will know from the lectures - are used for inserting into and removing from the map.

`insert` takes a key and a value, and what it does depends on whether or not there is already an item in the map with
the given key. If there is, then that mapping is updated to map the key to the new value. (In this case, the number of
mappings in the map - i.e. its length - doesn't change.) If the key is not already mapped to a value, then the mapping
is simply added, increasing the map's length by 1. (Note that in some map implementations, these operations will be
split out into multiple, more specific operations that assume whether or not the key is already in the map.)

`remove` takes a key, removes the associated mapping - decreasing the map's length by 1 - and returns the value that
the given key was mapped to. If the key was not in the map, then it instead raises a `KeyError`. (Some map
implementations that don't return the value of the removed mapping will instead just do nothing if the key was not in
the map - and similarly for other data structures, such as lists, if their `remove` does not `return` what was removed.)

The above is true for all the map types we will implement.

For this specific map, implemented using an unsorted array - just an array*, really, but we describe it as unsorted to
distinguish it from the next exercise's implementation - they work like this:

\* Well, not _just_ an array: it must be some form of array list, as we will want to insert/remove to/from it. Here
we'll use a `StaticArrayList` for simplicity, but you could just as well use a `DynamicArrayList` and improve some
efficiencies. This map wouldn't necessarily be implemented any differently, though, as long as you `insert_last` rather
than e.g. `insert_first`.

`insert` must first look through the already-contained mappings. If it finds one that shares the same key as the one to
be added, it updates it to map to the new value. Otherwise, if it has checked all the mappings and found none with the
given key, then it simply makes a pair containing the given key and value, and appends that to the end of the array
list. (Technically, you could insert it anywhere, but - as mentioned in the note above - if we were using a
`DynamicArrayList` then the difference would matter. Of course, with the `StaticArrayList` that we're using, and if we
were instead using a `CircularDynamicArrayList`, `insert_first` would be just as good.)

`remove` checks through each key/value pair in the array list, and once it finds the right pair, i.e. the one with the
right key, it removes that pair from the array list. If it reaches the end of the list without finding such a pair, it
raises a `KeyError`.

Okay, good luck! This penultimate exericise is easier than the final one, but is good for getting to grips with what the
operations are and what they're supposed to do, ahead of improving the relatively simple/naive implementations of this
exercise in the next.

---

Next:
- [Sorted Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/sorted_array_map/README.md)
