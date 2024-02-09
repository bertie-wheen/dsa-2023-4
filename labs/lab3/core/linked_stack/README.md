# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 3: More Lists, Stacks & Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/README.md))

### [Linked Stacks](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/linked_stack/README.md)
```shell
python labs linked_stack
```

Stacks are an important, widely-used data structure. The terminology of stacks, particularly the naming of the "push"
and "pop" operations, comes from spring-loaded plate dispensers found in buffets and restaurant kitchens.

The mechanism looks like this:

![An image of a plate dispenser mechanism.](https://www.cateringhardwaredirect.co.uk/cdn/shop/products/plate-dispensers-unheated-adjustable-plate-dispenser-291477.jpg)

They're mounted in counters, and then look something like this:

![An image of a pair of plate dispensers mounted in a counter. One of the dispensers is loaded with plates, and the other has none.](https://www.elakeside.com/foodservice/wp-content/uploads/sites/22/991FS.jpg)
(Note that the top-right dispenser is the equivalent of an empty stack!)

With these dispensers, you only really have access to the top of the stack, and can basically do one of three things:
1. See the plate on top of the stack if there is one, or otherwise see that the stack is empty.
2. Push a new plate down onto the top of the stack.
3. Pop the top plate off the stack (assuming there is one).

These map pretty well onto the basic stack operations of the abstract data structure. There are, however, a few
differences between these physical mechanisms and stacks as used in programming.

The first is that, though similar mechanisms exist for things like trays (and bullets - many magazines work like this),
we generalise much further and allow the items in a stack to be anything - not just plates.

The second is that this is perhaps a worse physical analogy than a simple stack of things, say books:

![An image of a stack of books.](https://cdn.pixabay.com/photo/2018/04/22/22/25/book-3342628_1280.png)

This is because although plate dispensers are where the *names* push and pop come from, the operations themselves don't
map exactly. When you push a plate onto the dispenser, the other plates move down. In programming, this doesn't happen -
when you push onto (or pop off) a stack, the other items don't move about in memory,* and so the book analogy is closer
to the mark.

\* (Technically if you're implementing a stack using a dynamic array list - which we will in the next exercise - pushing
_can_ cause the items to change addresses, but this doesn't necessarily happen, and happens in a very different way. The
analogy in this case could be that the stack of books has reached the roof, and thus you need to move them all into a
room with a higher ceiling.)

(In fact, the names push and pop don't even make sense with the plate dispenser analogy, as many of them - at least
these days - don't work that way, as they have a different sort of spring system: instead you simply place and take the
plates, and their weight does the rest.)

The third difference is that, although some stack implementations will only support the basic operations
(`stack.is_empty()`, `stack.peek()`*, `stack.push(item)`, `stack.pop()`), others will include some auxiliary ones (such
as for getting the number of items in the stack, iterating through those items, etc.). In the plus exercise
`virtual_stack_machine` (if you choose to do it), we'll additionally implement a few more stack operations: One for
moving the top item further down in the stack, another for moving an item further down in the stack up to the top (note
that both of these work well with the books analogy, but not the plates one), and finally one that duplicates the top
item (the physical analog of which could be pushing the same item as the one on top onto the stack).

\* The operation `peek`, for checking what the top item is without removing it, might - though this is only a guess -
also have its name come from plate dispensers. Often they will have lids on (as in the following image), to help keep
the plates clean (and potentially help with heat retention, as many of them also warm the plates). To see the top of the
stack, you'd therefore need to lift the lid and peek underneath.

![An image of a unit with a pair of plate dispensers. The left one has a lid covering it.](https://www.victoronline.co.uk/wp-content/webp-express/webp-images/uploads/2022/10/MPN20500.png.webp)

Stacks, like lists, are an interface, rather than a particular implementation of that interface. We're going to
implement that interface in two, quite different ways. In this exercise, we're implementing the stack interface
in a linked manner. This can be in much the same way as we implemented linked lists (have the stack reference the top
node, and each node the one below), but since we've already implemented linked lists, rather than essentially
copy-pasting their code and renaming a few things, we're instead going to use our implementations of them. (If you
haven't managed to implement them yourself yet, don't worry, as now the solutions have been released our code will use
that.)

Specifically, we're going to use a singly-linked list, as for the basic stack operations doubly-linked lists provide no
benefit (and actually have somewhat - though not asymptotically - worse time and space requirements). (Our stack will
additionally implement `iterator` and `reverse_iterator`, and doubly-linked lists would provide a slightly better
`reverse_iterator`, but since it's a relatively unimportant operation for many use cases, and the difference isn't
particularly drastic anyway, we prefer singly-linked lists.)

The class `LinkedStack` will store only one thing, namely a reference to an internal `SinglyLinkedList`, which it will
use to store its items and implement its operations. Each of the stack operations will be implemented by calling a
corresponding method on the stack.

You are to implement:
- `push`
- `peek`
- `pop`

(Each of these can be implemented in a single line.)

For this, and really any stack implementation, `push`, `peek` and `pop` should run in $\mathrm{O}(1)$ time using
$\mathrm{O}(1)$ space. You should find, however, that we essentialy get these efficiencies for free from our
singly-linked list implementation. (That is, if you decide correctly which linked-list operations to use!)

The following does somewhat give the game away, but it is still worth mentioning, and that is that we could just as well
use a different singly-linked list implementation that didn't choose to include a `_last` attribute, as that doesn't
gain us any efficiency, and in fact makes our stack very marginally slower and larger that it needs to be (and if we
were being like the - admittedly relatively few - stack implementations that don't want to support `length`, we could
also do without its `_length` attribute).

---

Next:
- [Array Stacks](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab3/core/array_stack/README.md)
