# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/README.md))

### [Static Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/static_array_list/README.md)
```shell
python labs static_array_list
```

Linked lists are great, but they do have some drawbacks. Particularly, they're no good for random access, which is the
getting/setting of items at arbitrary indices within the list.

Say you want to get the item at index 9, then the item at index 2, then 5. (Or 9000000, then 2000000, then 5000000.) You
can improve the efficiency somewhat through cleverness such as, after having got the node at index 2, and retrieved its
item, getting the node at index 5 not being starting at the beginning again and working through, but by starting at that
index 2 node and thrice traversing to the next node. (This means only 3 traversals, half of what's needed otherwise.)
However, the performance improvement to be had by doing this is fairly marginal. Not that it couldn't be noticeably
better, but at the end of the day it still takes linear rather than constant time.

Fundamentally, the problem is that `get_at(index)` and `set_at(index, new_item)` are $\mathrm{O}(n)$. In this exercise,
we implement the list interface using arrays, a type for which those operations are $\mathrm{O}(1)$.

The array-based list we'll implement is best suited for situations in which its size will be mostly static - i.e. only
rarely will its length change, with the majority of operations being e.g. `get_at` and `set_at` rather than `insert_at`
and `remove_at`.

We will start next week's lab by implementing two more array lists that are better suited for lists which are to be more
dynamic. Those implementations are the sort you'll usually find your favourite language's standard array list is.

This sort, however, is a useful stepping stone en route from arrays to them. It is a little simpler, and it introduces
the basic idea, which they then extend and improve some of the efficiencies of. It is not purely a stepping stone,
though - the static array lists we'll implement in this exercise do have some merit, in that they are smaller (i.e. they
take up less space) than those dynamic sorts. Thus, though most day-to-day programming is done with them, in an
environment with severely constrained storage capacity, you might find that this suits you better. Admittedly though,
the difference in size is very small, so it's relatively rare that you'd actually reach for this data structure. Still,
it is useful to think about and understand ahead of next week.

Arrays themselves aren't really a thing in Python, so we've provided an `Array` type for you to implement
`StaticArrayList` in terms of, which looks like:
```python
class Array(Base[Item]):
    """
    A basic array type, supporting O(1) random access.

    Space: O(self.get_length())
    """

    def __init__(self, length: int = 0) -> None:
        """
        Initialize this array.

        If ``length > 0``, the items will be initially ``None``.

        +--------+-----------+
        | Time:  | O(length) |
        +--------+-----------+
        | Space: | O(length) |
        +--------+-----------+

        :parameter length: the length of the array
        """
        ...

    @staticmethod
    def build(items: Iterator[Optional[Item]]) -> "Array[Item]":
        """
        Build an array containing the given items.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: an array of those items
        """
        ...

    def get_length(self) -> int:
        """
        Get the number of items in this array.

        ``None``s are counted as items.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        ...

    def get_at(self, index: int) -> Optional[Item]:
        """
        Get the item at the given index in this array.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the index
        :returns: the item at that index
        :raises IndexError: unless ``0 <= index < length``
        """
        ...

    def set_at(self, index: int, new_item: Optional[Item]) -> None:
        """
        Set the item at the given index in this ar.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the item's index
        :parameter new_item: the new item to overwrite the old item at the index with
        :raises IndexError: unless ``0 <= index < length``
        """
        ...

    def iterator(self) -> Iterator[Optional[Item]]:
        """
        Get a forward iterator over the items in this array.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the array's items, first-to-last
        """
        ...

    def reverse_iterator(self) -> Iterator[Optional[Item]]:
        """
        Get a reverse iterator over the items in this array.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the array's items, last-to-first
        """
        ...
```

(The implementations are removed, as their details aren't important.)

This array type implements (essentially) the static sequence interface from the lectures, which was:
```
 build(X)
.len()
.get_at(i)
.set_at(i, x)
.iter_seq()
```

(The - very slight - differences are a subset of those already discussed in this lab's introduction, when talking about
the dynamic sequence interface.)

You can probably see that it's partway to being a list (or dynamic sequence), but is just missing `insert_at` and
`remove_at` methods. (And e.g. `get_last`, but `get_length()` is $\mathrm{O}(1)$ so e.g. `get_at(get_length() - 1)` does
the trick, and moreover there aren't any specific implementations of the `_first`/`_last` variants that are better than
simply calling the general method.)

The idea is that `StaticArrayList` will contain an `Array`, and for methods like `get_at`/`set_at` just defer to the
array's implementation of them. For `insert_at`/`remove_at`, it will allocate a new array, one item larger/smaller than
the old one, and copy the items across from the old array to the new one. Some of the items will change indices, and for
`insert_at` the new item will also be added, and for `remove_at` the item to be removed won't be copied across.

One thing to note, which is just an effect of the way in which we've implemented `Array`, and not intrinsic to the type,
is that it will contain `Optional[Item]`s rather than `Item`s. This is so that it can be initialised with `None`s, but
in a different setting, say if you just wanted an array of `int`s, they could be initially `0`, and thus it could store
`int`s rather than `Optional[int]`s. (There are pros and cons, as with everything.)

However, in `StaticArrayList`, we can know that all the items in the arrays it contains are `Item`s - at least once
they're constructed, as e.g. immediately after allocating a larger array in `insert_at` it will contain `None`
placeholders, but then the old items will be copied across and the new item added, and it will then be full.
Therefore, because all the `StaticArrayList` methods maintain the invariant that all items are `Item`s rather than
`Optional[Item]`s, we can recover normal method signatures such as
```python
def get_at(self, index: int) -> Item:
```
rather than
```python
def get_at(self, index: int) -> Optional[Item]:
```

(In a language with more proper type checking, you might find you struggle to convince the typechecker of this, despite
knowing it will always be the case.)

Anyway, have a go at the exercise. As usual, the "boring" methods are already implemented, and the more interesting
ones - here, that's `insert_at` and `remove_at` - are up to you!

One final note, in case it's confusing (which it might be): `StaticArrayList` is a _dynamic_ sequence. Static sequences
are properly static, in that don't have any ability to change how many items they contain. `StaticArrayList` does, as it
has methods for inserting/removing items to/from the list. However, as these insertion/removal operations are
$\mathrm{O}(n)$, and next lab we'll implement different array lists for which they are (amortized) $\mathrm{O}(1)$,
this array list is better suited for situations in which the list is likely to be _mostly_ static.

To fully explain the name, it can be useful - for this, and for other types you'll encounter - to build it up backwards:
- `List`: This type is an implementation of the list interface. Remember that by "list" we mean "dynamic sequence", so
  we already know that it's going to support dynamic operations like `insert_at`.
- `ArrayList`: It implements the list interface by using arrays. (For `SinglyLinkedList` and `DoublyLinkedList`, their
  `LinkedList` suffix indicates that they implement the list interface by using linked-together nodes.)
- `StaticArrayList`: This array list is best suited for contexts in which it is likely to be predominantly static, i.e.
  most of the operations that will be performed on it will be e.g. `get_at`/`set_at`. (Next lab we will implement
  `DynamicArrayList`, which performs better when e.g. `insert_at`/`remove_at` are going to invoked very frequently.)

Going through it forwards: `StaticArrayList` is a type of array list, and an array list is a type of list.
Similarly, `SinglyLinkedList` is a type of linked list, and a linked list is a type of list.

Forwards, it gets progressively more general, and backwards, more specific.

Right, time to get into the code!
