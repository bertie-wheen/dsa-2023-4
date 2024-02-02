# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/README.md))

### [Loggers](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/logger/README.md)
```shell
python labs logger
```

It's often useful for a running program to keep a log of what's happening. You can then look back in this log and see
when particular things happened, or how many times they happened. If the program runs into an error, you can consult the
log to see what was happening just before the error that might have caused it, which can be very helpful for debugging.

There are countless logging libraries and frameworks out there, with varying amounts of bells and whistles, many of
which aren't always necessary even in the real world, at least for smaller projects - and especially here, given that
what we're interested in isn't so much all the details of the logging and loggers, but rather just in them as an example
of how you might use lists. The logger we'll look at, therefore is pretty minimal. (It's not absolutely minimal - the
simplest logger is just a print function!)

Logs are very often append-only. What that means is that new items are added exclusively to the end, and old items
aren't changed or removed. We won't go into _why_ this is, but it suffices to say that it enables other, desirable
properties, such as the ability to easily save to disk and/or compress a prefix of the log when it gets too large (or
periodically, regardless of size).

What's interesting about this property, from the perspective of this exercise, is that it means our logger will never
use the following operations:
- `set_first`
- `set_at`
- `set_last`
- `insert_first`
- `insert_at`
- `remove_first`
- `remove_at`
- `remove_last`

In fact, the only list operations our simple logger uses are `insert_last` and `iterator`!

(There are some reasons to use e.g. `get_at` if you want to e.g. perform binary search on the timestamps, but for the
sake of this exercise we're going to ignore that.)

(There's also a case to be made - not that we're going to make it - for using `insert_first` rather than `insert_last`,
if you want the most recent item to be first and iteration to be backwards in time.)

Given that these are the only operations we're using, they're the ones whose efficiency matters!

From our selection of lists that we've implemented, all three feature an $\mathrm{O}(n)$ time and $\mathrm{O}(1)$ space
`iterator`, but only `SinglyLinkedList` and `DoublyLinkedList` have an $\mathrm{O}(1)$ time-and-space `insert_last`,
with `StaticArrayList.insert_last` requiring $\mathrm{O}(n)$ time and space. The decision to be made, then, is between
`SinglyLinkedList` and `DoublyLinkedList`, and for our use-case and its minimal requirements, `DoublyLinkedList` doesn't
provide any benefit over `SinglyLinkedList`, and in fact is slightly worse: We're not using all those backwards links to
previous nodes that it stores and sets, so it takes more space and time.

Thus in this situation we would likely pick `SinglyLinkedList`, but if we decided to add e.g. `reverse_iterator`, we
might choose to switch over to using `DoublyLinkedList` instead. Luckily, because the list is wrapped and not directly
part of the `Log`'s interface, this is very straightforward, and can be done without users of the `Log` class needing to
make any changes to their code.

---

Next:
- [Character Generators](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/character_generator/README.md)
