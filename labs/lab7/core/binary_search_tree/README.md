# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 7: Binary Search Trees](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab7/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab7/core/README.md))

### [Binary Search Trees](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab7/core/binary_search_tree/README.md)
```shell
python labs binary_search_tree
```

Binary Search Trees (BSTs) are binary trees that store items in such a way that they can be efficiently searched through
when looking for particular items. (No prizes for guessing that that's where their name comes from.)

Their distinguishing feature that allows this is the storing of items in sorted order. (Sorted, that is, according to
the order of an in-order traversal.) Items in a BST are key/value pairs, and thus BSTs are essentially a type of "map"
data structure (and are therefore sometimes called tree maps). (Note that you can have BSTs where the items are just
items, in which case essentially they're their own keys, but we're not implementing that here.)

In labs 4 and 5, we implemented very different sorts of map (with very different characteristics), including hash maps.
As a refresher: Particular approaches to implementation aside, the abstract data structure of a map is one that "maps"
keys to values, and supports operations for modifying and accessing these mappings, for example a "get" (or "find")
operation that, given a key, returns the value associated with that key (if there is one). (Note that lists are, in a
sense, a type of map where keys - there called indices - are restricted to be only integers in a certain range.) Think
of the key as the id, and the value as the data. If you were a webserver, you might be given the id of a blog post, or a
user, and be asked for the associated data. To fulfill the request, you'd need some sort of map, where the keys are,
say, post ids, and the values are the actual posts (title, date, author, content, ...).

In a BST, then, the items - again, key/value pairs - are sorted according to their keys. (Because keys that are equal
are considered to be the same key, the keys form a strict total order, i.e. it's not just that the first item is less
than or equal to the second item, which is less than or equal to the third, but that the first item is less than - and
not equal to - the second, which is less than the third, and so on.)

The binary tree we were using as an example last lab,

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

is - if the letters are taken to be string keys - a BST.

That's because (sorting alphabetically)
```python
"a" < "b" < "c" < "d" < "e" < "f" < "g"
```
and that's the order in which they'd be visited by an in-order traversal.

The reason that this pattern of storage yields efficient search can be demonstrated by a simple example:

Say that we're looking for an item with key `"e"`. We start at the root, and are thus at the node/subtree (like last
lab, we're going to talk in terms of the latter, but you're free to think in terms of the former if you prefer) with
key `"c"`. `"c" != "e"`, and therefore this isn't the right subtree, and we must keep looking. But where to look? Since
`"c" < "e"`, thanks to the property of storing keys in sorted order, we know that the `"e"` subtree (if there is one)
must be a descendent of the right subtree. So we move to the right child, `"g"`. This again isn't `"e"`, but since
`"e" < "g"` our next step is to its left child, which does have the key `"e"`, and therefore we return the corresponding
value.

We only had to check three subtrees to find the right one, whereas if we'd been searching through a linked list, say,
we'd have had to visit five - and for larger trees, the benefit is much greater.

Admittedly, if we'd been looking for `"a"` we'd have had to visit two rather than one, but the point is that on average
you visit significantly fewer subtrees. The reason for this is that checking an item in a linked list only reduces the
remaining search space by one, but by checking a key in a BST we can narrow it down by up to half. This is because if
the key isn't the one we're looking for, we know whether we need to look in the left or right subtree, and whether or
not we find it there we never need to check the other subtree as we know it can't be there.

(If we were instead looking for `"h"`, we'd only need to check `"c"` and `"g"`. Because `"g" < "h"`, `"h"` could only be
in `"g"`'s right subtree, but since there isn't one, we can terminate the search and report that the tree has no mapping
for `"h"`.)

(You may have realised that what we're doing here is binary search! _This_ is where the name truly comes from: A binary
search tree is essentially the binary search algorithm done as a data structure. We will talk more about equivalences
between data structures and algorithms in the coming lectures and labs.)

As well as looking up key/value associations, we also want to be able to add or remove mappings to/from the structure.

When adding a new key/value mapping, there are two cases, based on whether or not there is already a value associated
with the given key. If there is, then the operation is very similar to search: Find the subtree with the given key, but
instead of returning its value, update it to the new value. If there isn't, then instead of updating an already existing
subtree, we need to insert a new one.

To do this, you follow the left/right child links based on which of the keys (the one we're adding or the one at the
(sub)root of the subtree we're visiting) is greater, in the same manner as before. You do this until you reach a subtree
that doesn't have the child you'd otherwise have moved to:

Say you were inserting a mapping from `"é"` to some value (where `"e" < "é" < "f"`). You'd start at the root, `"c"`, see
that `"c" < "é"` and move to its right child `"g"`. `"é" < "g"`, so move to `"g"`'s left child, `"e"`. `"e" < "é"`, so
right to `"f"`. `"é" < "f"`, so we would move to `"f"`'s left child, but it doesn't have one.

At this point, you've found where to insert the new mapping, so you'd make a subtree representing it, connect it to the
`"f"` subtree by setting the right attributes (the `"f"` subtree's `_left` and the new subtree's `_parent`), after which
the tree would look like this:

![(() a (b)) c (((d) e ((é) f ())) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_search_tree/inserted_e_acute.png)

This, and the other operations in this exercise, are much as they are described in the lectures. One difference is that
we maintain the length of the tree in a `_length` attribute to enable an $\mathrm{O}(1)$ `get_length()`, and
incrementing/decrementing this attribute at the appropriate times was elided from the pseudocode in order to more
clearly communicate the general idea of how the operations work (which is, after all, the most important thing).

Hopefully from the discussion above you're somewhat warmed up, and have started remembering what a BST is. Your task is
to now go back through the lecture slides (available on Canvas, as usual) and make sure you understand not just
insertion, but all the BST operations. _Then,_ understanding what they're supposed to do and how they're supposed to do
it, you should open up `exercise.py` and figure out how to turn that theoretical knowledge into actual code!

Before you do, though, we should mention a couple of things about the partial BST implementation you'll find in
`exercise.py`.

The first is that it's somewhat similar to last week's binary tree implementation, in that it's a "tree" class (in this
case, `BinarySearchTree[Key, Value]` rather than `BinaryTree[Item]`) and a "subtree" class (here
`_BinarySearchSubtree[Key, Value]` rather than `BinarySubtree[Item]`).

Also similar is that the methods on the tree class are generally simple wrappers around the subtree methods, which
contain the bulk of the implementation. The subtree methods are again usually implemented recursively - for example, if
you call `contains` on a subtree, it may call `contains` on one of its child subtrees, which may in turn call `contains`
on one of _its_ children, and so on, until the key is found (or isn't).

You'll notice, however, that our subtree class's name, `_BinarySearchSubtree`, is prefixed by an underscore. This, like
the other prefix underscores you've seen, indicates that it shouldn't be considered part of the public interface, and is
more an implementation detail than something users should directly access or modify. Whereas in the last lab we exposed
subtrees, and let users manually set their parents/children, in this lab we're going to be the ones deciding how these
links are set and thus what the structure of the tree is. The interface we're exposing to the users is very much like
that of the other maps we've implemented, with methods like `insert(key, value)` rather than e.g. `BinarySubtree`'s
`insert_right(subtree)`. They can use this interface to express _what_ they want to do, such as associate a value with
some key, and we'll figure out _how_ to do it (i.e. which subtree to update or add, and if we are creating and adding a
new subtree, we'll decide _where_ it should be added). This is because we want to maintain our sortedness and uniqueness
invariants, and letting users manually modify the structure of the tree impedes our ability to do that. It's also
because what the users really want, more than a BST, is a map. They want to think in terms of map operations, rather
than in terms of trees, and as we've mentioned before, they want to be able to easily swap the BST out for a different
map implementation if they find they want to.

Another difference between this and the previous lab is that, though we're still maintaining a `_length` attribute,
it's now on the tree itself rather than on each subtree. This is because neither we, nor the users, need to know the
length of arbitrary subtrees. _We_ don't because it's not important for the implementation of any of our operations,
and _they can't_ because they don't have access to the subtrees in the first place!

However, the methods you're asked to implement are again all on the subtrees, and are:
- `get_subtree`
- `get_minimum`
- `get_maximum`
- `get_previous`
- `get_next`
- `insert`
- `remove`

`get_subtree` is basically just `get` but it returns a reference to the subtree with the given key, rather than the
value - `get` (and other methods) can then be implemented in terms of it, by doing e.g. `get_subtree(key).get_value()`.

Before you get on with the exercise, a hint: You'll find we've included some methods called `ascend_left`,
`ascend_right`, `descend_left` and `descend_right`, and you may well find these useful in some of the methods you're
asked to implement.

Good luck!
