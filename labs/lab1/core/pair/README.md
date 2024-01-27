# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 1: Getting Ready](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/README.md))

### [Pairs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/pair/README.md)
```shell
python labs pair
```

This exercise, as with the previous, is somewhat artificial, but is just to show the sort of Python you need to be able
to read and understand. This one, though, is particularly similar to the real exercises you'll be doing from lab 2 onwards.

In the labs, we'll be implementing a lot of data structures, which we'll implement as classes.
These data structures will contain things, but what's important is how they structure those things, not what types of things they are. It doesn't matter whether they're `int`s, `str`ings, or whatever, what's important is how they are organised. We will therefore make the classes generic, i.e. parameterised over the type of things they contain.

For example, this exercise is a `Pair` of two things - they could be two `int`s, but just as well could be two `str`s.
By declaring the class as
```python
class Pair(Generic[Item]):
```
rather than
```python
class Pair:
```
we can then use the type variable `Item` in our type hints to describe the items it contains. (For a pair of `int`s, it
would be `int`, etc.)

This is arguably the most advanced feature we use, but you needn't worry much about it: it is only used in the type
hints, and has no impact on how the code itself runs. You're also not needed to write any type hints yourself, and
thus just need to know that, when you see the type `Item` (or in labs where we implement map types, `Key` and `Value`),
that it's not a specific type, but rather a parameter that stands in for whatever the type for that particular instance
is.

(If you want to use generics in your own Python, know that (a) `Item` is a `TypeVar`, (b) we've tucked our `TypeVar`s
away in a separate file to stop them from adding confusion/distraction for people who want to focus on the exercise
itself, and (c) in Python 3.12 there's been a lot of changes to all of this - see PEP 695.)

```python
@staticmethod
def build(items: Iterator[Item]) -> "Pair[Item]":
    """
    Build a pair containing the given items.

    +--------+------+
    | Time:  | O(1) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter items: an iterator of initial items
    :returns: a pair containing those items
    :raises ValueError: if the iterator contains more or less than 2 items
    """
    length = 0
    for item in items:
        if length == 0:
            first = item
        elif length == 1:
            second = item
        else:
            raise ValueError
        length += 1
    if length < 2:
        raise ValueError
    # noinspection PyUnboundLocalVariable
    return Pair(first, second)
```

In `build` there are three main things that need mentioning.

The first is the `@staticmethod` decorator, which makes `build` not a normal method, that you'd call on an instance of
the class (e.g. `pair.get_first()`), but a static method, that you call on the class itself (e.g. `Pair.build(items)`).
In fact, in this case you not only don't need an instance to call it on, but you get an instance from calling it, as
what `build` does is to build a pair containing the given items, as essentially an alternative constructor. This is a
litte awkward and unnecessary for `Pair`, as an `Iterator` can have any number of items, but `Pair` specifically two,
but we include it as the other data structures will have similar `build`ers that take an iterator and return an
instance.

The second is that in the type hint for the return type, `Pair[Item]` is enclosed in quotes. This is because it's what's
called a "forward reference", and we're not going to explain it, but basically just ignore the quotes and read it
without them.

The third is the line `# noinspection PyUnboundLocalVariable`. For reasons we're not going to explain, the line after
it - `return Pair(first, second)` - would cause PyCharm to warn us that `first` and `second` might be used before
they're assigned to, but since we know that they definitely are assigned to before they're used, we disable the warning
by putting this on the previous line. The main point of mentioning this is that you might see a similar comment -
`# noinspection PyProtectedMember` - in the other exercises. (A different warning, a different reason, but similarly
we're telling PyCharm that we know what we're doing and it's okay.)

There are a couple of methods for you to implement to make the test framework happy - `set_second` and
`reverse_iterator` - and then you're done! Before next lab, however, you may wish to learn some more Python, depending
on where you're at with it. See you next week!
