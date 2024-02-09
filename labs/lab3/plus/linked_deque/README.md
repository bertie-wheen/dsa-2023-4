# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Linked Deques](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/linked_deque/README.md)
```shell
python labs linked_deque
```

Is it a stack? Is it a queue? No! It's a *deque*.

With a stack, you add to one end, and remove from that same end. With a queue, you add to one end, and remove from the
other. With a deque, you can add or remove efficiently from either end. (You can, therefore, implement both stacks and
queues using deques.)

"Deque" is short for "double-ended queue", and is pronounced "deck". It's a useful pronunciation, because a good analogy
can be found in a deck of cards.

Imagine holding a deck of cards. You can very easily remove the card at the front, or the one at the back. Similarly,
you can easily add that card to the front or back of the deck.

(You can of course add and remove from anywhere in the deck, but less easily.)

In a deque, rather than a "top" or "front" item, we have "first" and "last" items. Rather than one pair of `push` and
`pop`, or `enqueue` and `dequeue`, we have two: `insert_first` and `remove_first`, and `insert_last` and `remove_last`.
Instead of `peek` or `front`, we have both `get_first` and `get_last` for checking those items.

Like stacks and queues, deques simply describe an interface, but can be implemented in multiple ways, so we'll similarly
implement them using first a linked list and then an array list.

You'll notice that `LinkedDeque` contains a `DoublyLinkedList` rather than a `SinglyLinkedList`. This is because, even
with a `_last_node` member, singly-linked lists can't remove efficiently from both ends, and so deques can really only
be implemented using doubly-linked lists (particularly because their operations are expected to run in - at least
amortized - constant time).

(You should find this (and the next) exercise very straightforward, having completed this labs' core exercises. They are
less to challenge, more because they're a good data structure to be aware of.)

---

Next:
- [Array Deques](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/plus/array_deque/README.md)
