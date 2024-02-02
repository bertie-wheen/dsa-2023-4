# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/README.md))
```shell
python labs 2
```

In this second lab - the first proper lab - we're going to be implementing lists. These are also called sequences, for
example as in last week's lectures. In these labs we're using the term "lists" instead, as that's the word you're more
likely to encounter when looking through languages' standard libraries. "Sequence" is often preferred in more
theoretical settings, such as the lectures, in which you're learning the abstract theory and concepts of the data
structures and algorithms in this module. These labs, though, are about their practical side, as we're going to be
programming them (and - in plus exercises - with them). At the end of the day, they're synonyms, and understanding the
concepts, their properties and efficiencies, and how they work, is much more important than the word you choose to use.

The lectures and these labs won't always line up exactly - they cover the same data structures and the same algorithms,
but each with a slightly different focus. The correlation between the two should be fairly obvious, but we we will try
to mention when there are little differences like this, so that when you're working on the exercises you can be sure
which bits of the lectures to refer back to. In this case, more specifically, what we're calling lists are what the
lectures call "dynamic sequences". (We're not going to be implementing static sequences, but we will be using an
implementation of them in the third exercise.)

Lists are a (almost _the_) fundamental data structure, and are used particularly frequently in all sorts of programming.
A list is simply a sequence of zero or more things (generally called _items_ or _elements_ - we'll call them "items"),
which is a pretty common thing to want to represent. You might have a list of tasks in a TODO-list app, a list of
highscores in a game, or a list of errors in your program's output!

All data structures have associated operations; for lists, we want to be able to add items (to the beginning or end, or
anywhere inbetween), swap items out for other ones, know how many items there are, retrieve those items (either
individually or by iterating through them), and remove them. Notice, though, that we've defined _what_ we want to be
able to do with a list, but we haven't defined _how_ it should be implemented in code or represented in memory. Lists
(along with many other data structures) can, in fact, be implemented in a number of quite distinct ways, with each
having relative advantages/disadvantages over the others.

In this lab, then, we'll implement three different sorts of lists. The first two are linked lists, and the third an
array list. (We will implement a couple more array lists next lab.) Linked lists implement the list interface using a
sequence of linked-together nodes, and array lists - unsurprisingly - using arrays.

We'll define the list interface to be following, and the lists we implement will be lists by the virtue of them
implementing at least these methods:
```
build            (items: Iterator[Item])            -> List[Item]
contains         (self, item: Item)                 -> bool
is_empty         (self)                             -> bool
get_length       (self)                             -> int
get_first        (self)                             -> Item           ! EmptyCollectionError
get_at           (self, index: int)                 -> Item           ! IndexError
get_last         (self)                             -> Item           ! EmptyCollectionError
set_first        (self, new_first_item: Item)       -> None           ! EmptyCollectionError
set_at           (self, index: int, new_item: Item) -> Item           ! IndexError
set_last         (self, new_last_item: Item)        -> None           ! EmptyCollectionError
insert_first     (self, new_first_item: Item)       -> None
insert_at        (self, index: int, new_item: Item) -> Item           ! IndexError
insert_last      (self, new_last_item: Item)        -> None
remove_first     (self)                             -> Item           ! EmptyCollectionError
remove_at        (self, index: int)                 -> Item           ! IndexError
remove_last      (self)                             -> Item           ! EmptyCollectionError
iterator         (self)                             -> Iterator[Item]
reverse_iterator (self)                             -> Iterator[Item]
```

(Note that the `!` is not Python notation, but we use it here to represent possible errors that methods might raise.)

(Note also that in the return type of `build`, `List` should be substituted for whatever the specific type of list is -
for example, `SinglyLinkedList.build(items)`, where `items` is an `Iterator[Item]`, will return a
`SinglyLinkedList[Item]`.)

The `_first`/`_last` variants of the `get`/`set`/`insert`/`remove` methods do what you might expect. They're usually
somewhat redundant, particularly `_first` methods, as instead of e.g. `list.remove_first()` you can write
`list.remove_at(0)`. The `_last` methods are more important for lists where `get_length` runs in worse than constant
time, as then e.g. `list.set_last(new_last_item)` can be much quicker than
`list.set_at(list.get_length() - 1, new_last_item)`. (Incidentally, note that `insert_last` is a little different from
the other `_last` methods, as `list.insert_last(new_last_item)` isn't equivalent to
`list.insert_at(list.get_length() - 1, new_last_item)` but rather `list.insert_at(list.get_length(), new_last_item)`.)
For all the lists we'll implement, however, `list.get_length()` will be $\mathrm{O}(1)$ and fast, so you might think
these specialised variants unnecessary, and to an extent they are. The reason we include them is both because from a
user's point of view `list.remove_last()` reads better - and communicates intent better - than
`list.remove_at(list.get_length() - 1)`, but also because sometimes there are much nicer, simpler implementations
possible than for the general method. The other reason is that we'll be writing the methods' efficiencies in their
docstrings, and having these particular cases as methods gives us a nice opportunity to describe their performance -
this is particularly important because often people will exclusively (or near-exclusively) access/modify the first/last
items, and (essentially) never items in the middle of the list.

Another thing to mention before diving in the exercises is the correlation between the list interface defined above
and the dynamic sequence interface defined in the lectures, which was
```
   build(X)
  .len()
  .get_at(i)
  .set_at(i, x)
  .insert_first(x)
  .insert_at(i, x)
  .insert_last(x)
  .remove_first()
  .remove_at(i)
  .remove_last()
  .iter_seq()
```

(The prefixed dots are to indicate that most of the operations are methods, i.e. are called on a list, e.g. `l.len()`,
whereas the first is just a function - it isn't called on anything, e.g. just as `build(X)`, and returns a list.)

You should be able to see that the interfaces are much the same. A couple of the operations have slightly different
names - `get_length == len`, `iterator == iter_seq` - but behave the same. The list interface additionally includes
some extra methods. A few of these are simply specialisations (`get_first` and `get_last` of `get_at`, and `set_first`
and `set_last` of `set_at`), as discussed above. The few extra that are more novel are `contains`, `is_empty` and `reverse_iterator`. The first two are included because they're particularly useful in practical contexts - for example,
in our implementations of the other operations we'll often need to know whether or not the list is empty. This need is
more general than lists, and in the other data structures we'll cover in later labs we'll include `is_empty` for the
same reason. `contains` is also a very general method amongst containers (such as lists, and other types we'll get to),
and is very useful for programming with them. We include `reverse_iterator` partly for completeness, and also because
it's an interesting exercise to find an $\mathrm{O}(n)$ implementation of for singly-linked lists, and also as a point
of comparison with doubly-linked lists. You will therefore be asked to implement it in the first two exercises of this
lab, but since it isn't covered in the lectures, you don't _have_ to. (Perhaps look at the solutions when they're
released next week, though.)

1. [Singly-linked Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/singly_linked_list/README.md)
2. [Doubly-linked Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/doubly_linked_list/README.md)
3. [Static Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/static_array_list/README.md)
