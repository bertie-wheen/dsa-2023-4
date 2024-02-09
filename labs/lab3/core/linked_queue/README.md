# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Linked Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/linked_queue/README.md)
```shell
python labs linked_queue
```

Though you may not have experienced the spring-loaded plate dispensers that are an analogy for stacks, you are likely
intimately familiar with the workings of queues.

Queues are processed from the front, and joined from the back. This means that they work in a first-in, first-out (FIFO)
manner, whereas stacks operate in a last-in, first-out (LIFO) style. (The person at the front of a queue joined it
before the people behind them, whereas the plate on top of the stack was put there after those below it.)

Of course, queues as a data structure can be of all sorts of things, rather than just people or cars. We also generally
don't account for queue-jumping or queue-leaving (except from the front).

The operation for adding an item to the back of a queue is called `enqueue`, and the one for removing an item from the
front is called `dequeue`. Similarly to how stacks have `peek` for seeing what item is on the top of the stack, queues
have `front` for seeing what item is at the front of the queue. (You might think that `peek` should be called `top`, and
sometimes it is - in fact nearly every operation we've covered and will cover goes by a number of names...)

The exercise itself is very similar to the `LinkedStack` one, in that we again wrap a `SinglyLinkedList`. This is only
because we included a `_last` attribute - otherwise, it would be better to wrap `DoublyLinkedList`.

Again, there are three methods to implement, but each requires only a single line. They are:
- `enqueue`
- `front`
- `dequeue`

Much as with stacks, queues assume not only that their core operations are implemented, but that they are efficient:
`enqueue`, `front` and `dequeue` should be (at least amortized) constant-time (and -space).

---

Next:
- [Array Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/array_queue/README.md)
