# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/README.md))

### [Singly-linked Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/singly_linked_list/README.md)
```shell
python labs singly_linked_list
```

In a singly-linked list of $n$ items, there are $n$ "nodes", one per item. Each node, as well as containing an item,
contains a link to the "next" node in the list. All the list itself then has to do is to keep track of the first node,
and it's able to reach any node, and thus any item.

For example, say you wanted to get the third item of a singly-linked list (and assume that there are at least three
items in the list) - if you start at the first node, ask it what the next node is, and then ask _that_ node which the
next node after _it_ is, you'll be at the third node, and its item will thus be the third in the list.

A singly-linked list, in its purest, most minimal form, is just this: A list points to its first node, and a node to the
next. (Note that these pointers are optional, in that they either point to a node or to nothing* - if a list is empty,
there is no first node, and similarly if a node is the last, then there is no next node.) However, there are a few
additional things that singly-linked list implementations will often add one or more of.

\* (Some implementations of singly-linked lists will instead point to dummy "sentinel" nodes that don't hold an item but
instead mark the end of the list, with doubly-linked lists sometimes also having one that marks its start. However,
these are unnecessary, increase the space required to store the list, and are - to a certain taste - inelegant. That
said, advocates for the approach would say that enable elegant ways of coding certain things. We're not going to
discuss all the pros/cons in detail, and basically it's subjective - the brief mention here is in case you see other
linked-list implementations that have these dummy nodes, and because when we get onto tree structures later in the
module, some implementations do the same thing there, but we will again choose not to.)

The first of these is for the list to store its length - that is, how many items are in it. Without this, getting the
length of the list requires an entire traversal of it - starting at the first node, moving to the second, the third, etc
and counting them up as you go. This approach takes time linear in the length of the list - the bigger the list, the
more time required to calculate its length. That is, the time it takes to get the length is essentially proportional
(plus or minus some constant factors and other lower-order terms) to that length.

If the list keeps track of its length, then getting that length is a trivial, constant-time operation. If you have two
lists of different sizes - one very small, one very large - then getting their length takes the same amount of time, as
the time required to read a variable holding the length doesn't depend on how many items there are. The duration may
vary a little between reads, depending on e.g. whether that variable's in the cache at the time it's read, but point is
that there's a maximum duration that it'll always be less than, and that maximum is the same regardless of $n$.

There is a downside, and it's essentially the same tradeoff for the other additional things about to be mentioned.
The first part of it is that storing more data requires more space. However, we're only storing one extra number per
list, and usually what you have many of is nodes/items, rather than lists. If you had unusually many lists, then this
could start to add up, and if the lists were generally very small - perhaps not more than a couple of items each - then
it could represent a significant fraction of the total space required. Generally though (and this becomes truer the
larger $n$ becomes), it's not enough for that to matter. Usually what matters isn't space, but speed. There are
exceptions, of course, such as in embedded environments, but in the modern world where you can buy RAM for £1-2/GB and
HDDs for 1-2p/GB, an increase in storage requirements can often be worthwhile if it buys a decrease in execution time.

However, the other part of the downside is that, despite speeding up some operations - in this case `get_length` -
it slows down others. This is because now, when we are inserting or removing an item, we have to increment or decrement
the variable containing the current length. This too, though, is rarely a price not worth paying. The addition of one
increment - a constant-time operation, and a quick one at that - to `insert_at` - generally a linear-time operation -
doesn't affect its performance, asymptotically (it remains linear) or practically (even for small $n$, it's only a small
amount of extra time as a fraction of what was already required).

As well as a variable for tracking the length of the list, we will also add one for tracking its last node. Again, some
singly-linked list implementations will only track the first, but adding this extra link from the list to the last node
doesn't stop it being a singly-linked list (the "singly" is referring to how many links the nodes have, not the list),
and - just like with the length - its addition improves the time efficiency of some operations - specifically
`get_last`, `set_last` and `insert_last` - from linear to constant. In each case you would otherwise have to traverse
the entire list to get to the last node. (Unfortunately it doesn't have the same effect on `remove_last`, as that method
requires modifying the second-last node to stop it pointing at the now-removed last node, which is no longer next, and
thus we must traverse the list to get to it.)

The third thing we'll add is a pointer from each node to the list it's in. This is certainly the least-standard and
most-debatable of the three, but we do it because it enables quite a nice interface, and for us to implement methods on
the nodes themselves, rather than just on the list.

Without further ado, it's time to get into the actual code.

There are two classes: `SinglyLinkedList` and `SinglyLinkedNode`, and what they are should be self-explanatory.

They each have methods for you to implement, namely:
- `SinglyLinkedList`
  - `get_node_at`
  - `set_at`
  - `insert_at`
  - `remove_at`
  - `reverse_nodes_iterator`
- `SinglyLinkedNode`
  - `insert_previous`
  - `insert_next`
  - `remove_previous`
  - `remove`
  - `remove_next`

A word of advice before you do: The expected approach is that you implement most of the `SinglyLinkedList` methods in
terms of the `SinglyLinkedNode` ones. For example, `SinglyLinkedList.remove_at` should call `SinglyLinkedNode.remove`.
(You don't absolutely have to do it like this, but should find that they are more simply implemented if you do.) The
node operations (e.g. `insert_next`) aren't covered in the lectures, but they are useful both because there are things
that are impossible to (efficiently) do without them, and because - as just mentioned - the implementations of the list
operations are simpler if done in terms of them. (When we get onto trees in a few labs' time, we will similarly have
methods on their nodes, for the reasons just stated, and because those methods can be very elegantly implemented using
recursion on the nodes - and that recursion is more natural if the methods are actually on the nodes themselves. Anyway,
no need to worry about that quite yet!)

You also shouldn't worry about accessing `SinglyLinkedList` private members (e.g. `_length`) from `SinglyLinkedNode` -
normally it's not the done thing to use one class's from another, but in this case the two classes are so interdependent
that it doesn't matter. In languages like C++ you could declare them "friend" classes - Python doesn't have such a
mechanism, but one alternative for legitimising this would be to have `SinglyLinkedNode` be nested as an inner class
within `SinglyLinkedList`. However, as well as increasing the amount of Python knowledge required, there are one or two
other issues with inner classes (particularly with generics and type variables) that meant we've gone for the simplest
option, which is to add `# noinspection PyProtectedMember` before the `SinglyLinkedNode` class to suppress the warnings
PyCharm would otherwise give. If you want to use `SinglyLinkedNode` private members from `SinglyLinkedList`, you can add
another of these comments before it, but the reason we haven't is that there's no real need for it to, as it can just
use the getter and setter methods (such as `get_next_node` and `set`).

Right, it's time to have a go!

Implementing these operations is all about invariant maintenance: You can assume that all the attributes of the list and
nodes are correct before the operation you implementing, but need to make sure that they remain correct afterwards.
(This is an additional downside to the extra properties such as `_length` and `_last_node` - the more things there are
to update, the easier it is to fail to update one correctly.) As long as they do, and all the other operations similarly
maintain their correctness, then the assumption is safe to make, as the operations are the only places in which the
members are mutated - because they're private, users of the class won't modify them, meaning they remain correct between
operations.

Regarding efficiency, you should make sure that your implementation matches the specification in the docstring. You
should also - though this is less important - try not to have your operations do more work than necessary. If you need
only traverse the list once, then try not to traverse it twice, even if it wouldn't make a linear operation any worse in
Big-O terms.

Good luck!

---

Next:
- [Doubly-linked Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/doubly_linked_list/README.md)
