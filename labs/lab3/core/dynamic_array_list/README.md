# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Dynamic Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/dynamic_array_list/README.md)
```shell
python labs dynamic_array_list
```

When, last lab, we implemented the list interface by using arrays, we got $\mathrm{O}(1)$ random access - which is quite
desirable - but unfortunately had a somewhat off-putting $\mathrm{O}(n)$ append (`insert_last`).

This isn't much of a problem if the array is likely to be mostly static, in which case our `StaticArrayList` should
perform well enough - but what if we're going to be doing lots of `insert_*` and `remove_*` operations, and can't use
linked lists because we need fast random access?

In this exercise we'll implement dynamic array lists, which combine the best of both worlds, in that they have both
$\mathrm{O}(1)$ `get_at` and `set_at`, _and_ an $\mathrm{O}(1)$* `insert_last`.

\* Well, sort of $\mathrm{O}(1)$. Technically, "amortized" $\mathrm{O}(1)$, the meaning of which was explained in the
lectures and will be recapped in a moment.

Two quick notes regarding terminology: What the lectures call "dynamic arrays", these labs call "dynamic array lists",
and similarly what in the lectures is their "size" in these labs is their "capacity".

Dynamic array lists, like the static array lists we implemented last lab, are backed by internal arrays. The trick we
employ here is that that array can be larger than we need it to be. For the static array lists, their backing array is
always full, i.e. they are always at capacity, and thus to insert a new item must always reallocate. If their length
(the number of items stored) is $l$ and their capacity (the maximum number of items that can be stored without
reallocating) $c$, then for static array lists it is always true that $l = c$. For these dynamic array lists, however,
instead $l \le c$. That is, their array isn't necessarily filled, and thus they can have spare capacity, meaning that
new items can be inserted without having to reallocate a larger array.

The spare capacity is towards the end, and thus - like static array lists - if the new item is to be inserted in the
middle of the list, then some items will need to be shifted right. However, consider inserting an item to be 7th in a
list that currently contains 10 items. A static array list would need to allocate a new, 11-item array, copy the old 10
items across, and then add the new one. However, a dynamic array list can simply shift the last 3 items one position to
the right before adding the new one. Thus `StaticArrayList.insert_at` takes time linear in the length of the list,
however `DynamicArrayList.insert_at` (assuming there is spare capacity - we'll talk more about the effects of when it
isn't in a moment) is also linear, but in the difference between the index and the length of the list. The best example
of this is `insert_last`, which for `StaticArrayList` is $\mathrm{O}(n)$, and for `DynamicArrayList`s with spare
capacity $\mathrm{O}(1)$.

Of course, even if there is spare capacity, i.e. $l < c$, then after inserting enough (specifically, $c - l$) new items
there won't be - the array will be full, with $l = c$. At this point, like the static array list, the dynamic array list
must reallocate a new array with a larger capacity. The difference is in how much the capacity is increased by: Static
array lists increase the capacity by only 1, just enough to fit the new item. Dynamic array lists, however, usually
double their capacity. If there were 10 items, then the new array allocated to fit the 11th item will not be of capacity
11, but 20. Some will increase it by different amounts, but the increase will be always be proportional - they might
instead triple their capacity, but they won't increase it by a constant amount (e.g.  always making room for an
additional 8 items, regardless of how many there already are).

(Note that there is one exception to be borne in mind when e.g. doubling, and that is when the array list had zero
capacity, in which case doubling wouldn't increase it, and the new capacity should instead be some constant value, e.g. 1.)

The increase in capacity must be multiplicative (e.g. $\times 2$ or $\times 3$) rather than additive (e.g. $+1$ or $+2$)
for `insert_last` to be amortized $\mathrm{O}(1)$.

To see why, imagine starting with an empty dynamic array list, and appending to it repeatedly.

Initially, the length and capacity are 0. (Actually the capacity could be more than that, but let's assume it's 0 for
the sake of this example.)

In order to append to it, the capacity must be increased, as it is full. (Incidentally, note that in this specific case
the array is both empty and full!) Given the capacity is 0, doubling it won't work, so for this special case set it to 1
(or really any sensible "small" number, but we're going to pick 1). The dynamic array list internally reallocates a new
array of length 1, and then sets index 0 of this new array to be the appended item, and its (the list's) length
attribute to 1.

Appending to it again, it is again full, and so this time we double the capacity, allocating a new array of length 2,
copy the item at index 0 across, set index 1 to be the appended item, and update the length to be 2.

Next append, it is _still_ full, but now we double the capacity to 4, copy across the two pre-existing items, append the
third, and increment the length.

Now the dynamic array list's capacity is 4, but its length is only 3, so when appending the fourth item no allocating or
copying needs to be done. Instead, it just sets index 3 to be the new item, and updates the length attribute.

Thus far you may think that most appends cause reallocation and copying of the old items, but this is only for these
very small array lists - as the capacity grows, doubling (or otherwise multiplying by a constant factor) has more of an
effect, and means reallocations happen decreasingly often.

To save many more paragraphs of this, here's a table of what happens as we repeatedly append to the array:

| Old Length | Old Capacity | New Length | New Capacity | Reallocation? | Copies | Total Copies | Copies per Append |
|------------|--------------|------------|--------------|---------------|--------|--------------|-------------------|
|  0         |   0          |  1         |   1          | Yes           |  0     |  0           |  0 /  1 = 0       |
|  1         |   1          |  2         |   2          | Yes           |  1     |  1           |  1 /  2 = 0.5     |
|  2         |   2          |  3         |   4          | Yes           |  2     |  3           |  3 /  3 = 1       |
|  3         |   4          |  4         |   4          | No            |  0     |  3           |  3 /  4 = 0.75    |
|  4         |   4          |  5         |   8          | Yes           |  4     |  7           |  7 /  5 = 1.4     |
|  5         |   8          |  6         |   8          | No            |  0     |  7           |  7 /  6 = 1.17... |
|  6         |   8          |  7         |   8          | No            |  0     |  7           |  7 /  7 = 1       |
|  7         |   8          |  8         |   8          | No            |  0     |  7           |  7 /  8 = 0.875   |
|  8         |   8          |  9         |  16          | Yes           |  8     | 15           | 15 /  9 = 1.67... |
|  9         |  16          | 10         |  16          | No            |  0     | 15           | 15 / 10 = 1.5     |
| 10         |  16          | 11         |  16          | No            |  0     | 15           | 15 / 11 = 1.35... |
| 11         |  16          | 12         |  16          | No            |  0     | 15           | 15 / 12 = 1.25    |
| 12         |  16          | 13         |  16          | No            |  0     | 15           | 15 / 13 = 1.15... |
| 13         |  16          | 14         |  16          | No            |  0     | 15           | 15 / 14 = 1.07... |
| 14         |  16          | 15         |  16          | No            |  0     | 15           | 15 / 15 = 1       |
| 15         |  16          | 16         |  16          | No            |  0     | 15           | 15 / 16 = 0.94... |
| 16         |  16          | 17         |  32          | Yes           | 16     | 31           | 31 / 17 = 1.82... |
| 17         |  32          | 18         |  32          | No            |  0     | 31           | 31 / 18 = 1.72... |
| 18         |  32          | 19         |  32          | No            |  0     | 31           | 31 / 19 = 1.63... |
| 19         |  32          | 20         |  32          | No            |  0     | 31           | 31 / 20 = 1.55    |
| 20         |  32          | 21         |  32          | No            |  0     | 31           | 31 / 21 = 1.48... |
| 21         |  32          | 22         |  32          | No            |  0     | 31           | 31 / 22 = 1.41... |
| 22         |  32          | 23         |  32          | No            |  0     | 31           | 31 / 23 = 1.35... |
| 23         |  32          | 24         |  32          | No            |  0     | 31           | 31 / 24 = 1.29... |
| 24         |  32          | 25         |  32          | No            |  0     | 31           | 31 / 25 = 1.24    |
| 25         |  32          | 26         |  32          | No            |  0     | 31           | 31 / 26 = 1.19... |
| 26         |  32          | 27         |  32          | No            |  0     | 31           | 31 / 27 = 1.15... |
| 27         |  32          | 28         |  32          | No            |  0     | 31           | 31 / 28 = 1.11... |
| 28         |  32          | 29         |  32          | No            |  0     | 31           | 31 / 29 = 1.07... |
| 29         |  32          | 30         |  32          | No            |  0     | 31           | 31 / 30 = 1.03... |
| 30         |  32          | 31         |  32          | No            |  0     | 31           | 31 / 31 = 1       |
| 31         |  32          | 32         |  32          | No            |  0     | 31           | 31 / 32 = 0.97... |
| 32         |  32          | 33         |  64          | Yes           | 32     | 63           | 63 / 33 = 1.91... |

From this table, you can see that most of the time appending an item is a constant-time operation, only occasionally
requiring linear time (to do $n$ copies). Particularly, though, if you look at the rightmost column, you can see that on
average you're not doing more than 1 or 2 copies per repeated append. This means that we describe dynamic array lists'
append as "amortised" constant time. The verb "amortise" means to spread out the cost of something, such as spreading
the cost of an item over several payments. In this case, the cost isn't a number of pounds, but the number of copies. As
the array list grows, when we do need to increase the capacity we have to do more and more copies, but also as it grows,
we need to increase the capacity less and less often. The trick is that the increasing number of copies per reallocation
and the decreasing number of reallocations per append effectively cancel eachother out, and therefore append - not every
specific append, but the general append, considered across all its repeated invocations - is effectively constant time
(as the average number of copies is bounded above by the constant 2).

Clearly, amortised constant time isn't as good as "proper" constant time (it's constant time but with an asterisk and
accompanying terms, conditions and disclaimers). However it's worth noting that the difference can be really important:
If you're working on a realtime system, say, a game that must run at 60 frames per second, then if you're appending to
an array once per frame, some frames will be "unlucky" and do a linear-time append - and once the array grows large
enough, the frame will exceed its time budget of $\frac{1}{60}\mathrm{s} = 16\frac{2}{3}\mathrm{ms}$, and the game will
lag. (After that, though the time between lags will get longer, the lags themselves will also get longer.) For a game
this is not _too_ serious (I know, I know), but for certain realtime systems where lives are at stake this is absolutely
not an option. Therefore, in such cases it is important to be sure whether the operations you're using are _actually_
constant-time, or merely amortised constant.

Right, enough theory, let's get to the point of these labs: practical implementation!

In this exercise you're to implement:
- `resize`
- `insert_first`
- `insert_last`
- `insert_at`
- `remove_first`
- `remove_last`
- `remove_at`

You should be familiar with what the `insert_*` and `remove_*` methods are supposed to do, namely to insert or remove an
item at a given index. Still, there's the question of _how_ to do them. As explained above, `insert_*` methods should,
if necessary, reallocate a larger array (twice the size), before shifting along any items to the right of the given
index, to make room for the new item, which is then added.

The `remove_*` methods shift left any items to the right of the given index, and may also reallocate - not every dynamic
array list's removal methods do this, but ours will. If, with the item removed, the list is only a quarter full (or
less), then the capacity is halved. This stops the array list becoming space inefficient (and, as explained in the
lectures, avoids the problem caused by halving when half-full). The reason it's not _needed_ is that there is a method
`shrink_to_fit` (also called things like `trim_to_size`) that reduces the array list's capacity to its length, and thus
minimizes its size. However, this requires the user to manually call it, and thus also requires them to know that
they're using a dynamic array list, rather than just an arbitrary list, which makes it less straightforward to swap it
out for another type, e.g. a linked list, and similarly have trouble if swapping e.g. a linked list out for it, as
additional thought is then required about if and where `shrink_to_fit` calls are needed.

In both cases (insertion and removal) you should remember to update the length, and resizing should be done by calling
`resize`, the other method to be implemented. However, you need not call it directly - if you look through the class's
methods, you should find some written in terms of it that should be useful.

You may also find it useful to know that not only can you write e.g. `for index in range(length): ...` to iterate over
the numbers `0`, `1`, ... `length - 1`, but you can write e.g. `for index in reversed(range(length)): ...` to iterate
over those same numbers in reverse, i.e. `length - 1`, `length - 2`, ... `1`.

The `resize` method, given a new capacity (which must be enough to hold the list's items), allocates an appropriate
array, copies over the items from the old one to it, and swaps the list over to using that new array. (Unless, of
course, the list's capacity is already what's wanted, in which case it can just do nothing.)

As a reminder, as was said in the static array lists exercise, Python doesn't really have a proper array type, so we've
provided an `Array` type for you to implement `DynamicArrayList` in terms of, and it looks like:
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

The implementations are removed, because they don't matter. What matters is the interface - what you need to know is
what the methods are called (e.g. `get_at`), what parameters they take (e.g. `index`, an `int`), what they return (an
`Item`), what they're used for (getting the item at the given index), which exceptions they might raise and why (an
`IndexError` if the index is out of bounds) and the efficiency with which they run ($\mathrm{O}(1)$ time and space).
You get all of that from the methods' signatures and their docstrings. The implementations, which tell specifically
_how_ they do what they do aren't, in this case, important. In general, when you're "outside" a class, you shouldn't
worry about or depend on the internals of "how", but merely think in terms of the "what". You should treat external
classes or dependencies as black boxes, that do what they say on the tin but could change the way in which they do
that at any moment - and your code that uses them shouldn't break if they do, as long as they still correctly
implement their interface. Doing otherwise leads to very brittle code!

You can get straight on with the exercise now if you'd like, though if you're interested here are a couple of little
incidental notes for when you're programming with dynamic array lists in the real world:

In the wild you'll often find implementations that have methods called things like `reserve` or `ensure_capacity` that
might sound like they're just renamings of `resize`, but they actually only work in one direction - that is, they will
increase the capacity, but not decrease it. (A way around this, if needed, is to call `shrink_to_fit` first.)

A more important point: Dynamic array lists, including this one, can often be given an initial capacity parameter. This
is particularly useful in the (reasonably common) case of creating an empty array list and then appending loads of items
to it. If you know - at least roughly - how many items you're going to append in advance, then specify that number as the
initial capacity when you create the dynamic array list. The reason for this is, as you might imagine, that you can save
many reallocations and copies that would otherwise happen in the course of building up the list.

If you do specify the initial capacity, or manually `resize`, then the constraint mentioned in the lectures that
$capacity = \Theta(l)$ can be violated, but usually if you do that it's because you're about to add a load of items to
the list, meaning that it will be almost immediately be restored. (The same constraint can also be violated by dynamic
array list implementations that don't shrink when removing items from a mostly-empty list, but these usually expect that
you'll manually `shrink_to_fit` if it matters, and doing that will restore the property.)

---

Next:
- [Circular Dynamic Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/circular_dynamic_array_list/README.md)
