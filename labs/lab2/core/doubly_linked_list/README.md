# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/README.md))

### [Doubly-linked Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/doubly_linked_list/README.md)
```shell
python labs doubly_linked_list
```

Doubly-linked lists are much like singly-linked lists, but though a node in a singly-linked list only has a single link
(to the next node, its successor), a node in a doubly-linked list also has a second link (to the previous node, its
predecessor).

Additionally, all singly-linked list implementations include a pointer to the first node (if there is one), but only
some include a pointer to the last - all doubly-linked list implementations, however, include pointers to both.

These extra links do cause higher memory usage, as well as slightly slowing down some operations (as they need to be set
and re-set), but also result in significant, sometimes asymptotic speedups to other operations, that - depending on the
particular requirements of the use-case - can make doubly-linked lists a better choice than their singly-linked
counterparts.

By adding the pointer to the last node (which, again, is not an inherently doubly-linked list thing - some singly-linked
lists do this too), we improve the time efficiency of `get_last`, `set_last` and `insert_last` from linear in the length
of the list to constant (`O(list.get_length())` to `O(1)`), as we don't need to traverse the whole list to get to the
end of it.

However, in a singly-linked list, even with a pointer to the last node, accessing/modifying/etc the second- or
third-last remains $\mathrm{O}(n)$ (where $n$ is the length of the list), as there's no way to move backwards to those.
In a doubly-linked list, getting the second-last item is $\mathrm{O}(1)$: Get the last node, get its predecessor, get
the predecessor's item, done. None of that depends on the length of the list or any other variable factor.

The more general case of getting the item at an arbitrary index in the list takes linear time whether the list is
singly- or doubly-linked. However, if it's in the second half of the list, a doubly-linked list can be more than twice
as fast (potentially much more than twice if it's near the end). This is because it can start from the end and work
backwards, resulting in (maybe many) fewer nodes traversed. (Getting the item at index 999,990 in a 1,000,000-element
list is about 100,000x faster if it's doubly-linked rather than singly-linked.)

There are other speedups, notably `remove_last`, which is $\mathrm{O}(n)$ for a singly-linked list, but $\mathrm{O}(1)$
for a doubly-linked one.

There's also reverse iteration: Singly-linked lists can implement this in either $\mathrm{O}(n)$ time and
$\mathrm{O}(n)$ space or $\mathrm{O}(n^2)$ time and $\mathrm{O}(1)$ space. Doubly-linked lists, however, can implement
it in $\mathrm{O}(n)$ time and $\mathrm{O}(1)$ space.

As for the exercise, you've the same operations to implement as in the previous one:
- `DoublyLinkedList`
    - `get_node_at`
    - `set_at`
    - `insert_at`
    - `remove_at`
    - `reverse_nodes_iterator`
- `DoublyLinkedNode`
    - `insert_previous`
    - `insert_next`
    - `remove_previous`
    - `remove`
    - `remove_next`

But though the interface is the same, the implementation is not - and not just for the methods whose efficiencies
should be improved from linear- to constant-time. Even the others will require careful reconsideration, as there are now
`_previous_node` links to be kept correct. (They are only a performance-enhancing blessing to some methods because they
are updated by others.) You should also try to implement the second-half reverse-traversal speedup mentioned above for
the methods on `DoublyLinkedList` that take an index.

Other than that, things are similar to the previous exercise, so if you managed that, you should manage this. (Still,
don't hear that and become complacent: it is worth doing!)

---

Next:
- [Static Array Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/static_array_list/README.md)
