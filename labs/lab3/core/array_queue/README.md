# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Array Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/array_queue/README.md)
```shell
python labs array_queue
```

The last exercise of the lab! (Don't cheer too loudly... and anyway, there are some plus exercises if you're instead
disappointed by the news.)

Just as we implemented the stack interface by using both a linked list and an array list, and have implemented the queue
interface using a linked list, we now implement it using an array list. This time, though, instead of
`DynamicArrayList`, we'll use `CircularDynamicArrayList`. Otherwise - as was explained in the lectures - either our
`enqueue` or our `dequeue` would be $\mathrm{O}(n)$, and though the result would technically be a queue, it wouldn't be
a queue that many people would consider using. This way, both `enqueue` _and_ `dequeue` can be amortized
$\mathrm{O}(1)$.

You should again implement:
- `enqueue`
- `front`
- `dequeue`

Hopefully these shouldn't give you too much trouble (particularly having done the previous three exercises). Once you've
written the three lines required (unless you decide, for some reason, to implement them in more than a line each), you
_can_ stop, but are encouraged to have at least a little look at the plus exercises. (Though again, you're not
_expected_ to.) The first two are very much like these exercises, but instead implementing the "deque" (double-ended
queue) interface using both linked lists and array lists, and then there are two, more involved (but more interesting)
examples of applications of stacks and queues.
