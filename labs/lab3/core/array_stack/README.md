# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Array Stacks](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/array_stack/README.md)
```shell
python labs array_stack
```

In this exercise we'll again implement a stack, but this time by wrapping a dynamic array list rather than a
singly-linked list.

By completing the exercise, you should see how this is possible - however, you may be wondering why it is useful. The
main reason - explained here as it might not come through from the exercise itself - is that some stacks choose to
support not just `peek`ing at the top item, but (for example) `get`ting the $n$-th item. Our stack provides a "purer"
interface that doesn't include this, and therefore in this case you would likely choose the linked-list-based
implementation, but in such cases where random access is desired or required, dynamic array lists of course shine (that
being a main advantage of theirs).

Where `LinkedStack` contained a `SinglyLinkedList` that it delegated its operations to, `ArrayStack` similarly contains
a `DynamicArrayList`.

There are again the same three methods to implement:
- `push`
- `peek`
- `pop`

You'll find that their implementation is very similar to the previous exercise - though you should think afresh about
which operations on the wrapped list give the best efficiencies.

---

Next:
- [Linked Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/linked_queue/README.md)
