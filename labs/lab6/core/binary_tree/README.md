# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 6: Binary Trees & Traversals](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab6/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab6/core/README.md))

### [Binary Trees](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab6/core/binary_tree/README.md)
```shell
python labs binary_tree
```

We're implementing binary trees in this exercise.

As in the lectures, we're going to be implementing them in a linked style, however rather than talking about nodes,
we're going to be talking about subtrees - rather than having the classes `BinaryTree[Item]` and `BinaryNode[Item]`,
we're going to have `BinaryTree[Item]` and `BinarySubtree[Item]`.

This is simply because most of our implementation is going to be recursive methods on the subtrees, and it makes more
sense to talk about the length of a subtree than the length of a node, or whether a subtree contains a given item,
rather than if a node contains a given item. You might say that the length of a node is always 1, and it only contains
an item if that's the item on the node, rather than considering its descendants. You might instead say that the length
of a node is the length of the subtree rooted at that node, however it's more straightforward to simply talk about the
length of the subtree.

The `BinaryTree` class is going to essentially forward all of its methods to the root subtree, assuming there is one,
or otherwise return the appropriate values for an empty tree. Again, the bulk of the methods are going to be on the
`BinarySubtree` class, and many of these will work recursively, calling the corresponding methods on the left and right
subtrees, and combining the results.

The `BinaryTree` class contains only one thing: a reference to the root subtree (if there is one, or else `None`).

The `BinarySubtree` class, however, contains several things: the item at the root of the subtree, three references to
subtrees - specifically the parent, the left child and the right child, assuming in each case that it has them - and the
subtree's length and height.

The methods whose bodies you're asked to fill in are all on `BinarySubtree`, and they are:
- `contains`
- `get_level`
- `_calculate_length`
- `_calculate_height`
- `insert_left`
- `insert_right`
- `remove_left`
- `remove_right`
- `pre_iterator`
- `iterator`
- `post_iterator`
- `reverse_pre_iterator`
- `reverse_iterator`
- `reverse_post_iterator`

This may seem like a lot, but (a) this is the only core exercise this lab, and (b) many of them are very similar, so for
example if you figure out `insert_left` then you'll know how to do `insert_right`.

It's obviously important to be clear about exactly what the methods are supposed to do, so we're going to look at an
example binary tree and give what each of them should output in its case. That binary tree is

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

First though, it's worth mentioning how you'd create the tree in code in the first place, which would be to write:
```python
d = BinarySubtree(item="d")
f = BinarySubtree(item="f")
b = BinarySubtree(item="b")
e = BinarySubtree(item="e", left=d, right=f)
a = BinarySubtree(item="a", right=b)
g = BinarySubtree(item="g", left=e)
c = BinarySubtree(item="c", left=a, right=g)
tree = BinaryTree(root=c)
```

Here we're creating it bottom-up, which (for reasons we'll touch on later) is the style our binary tree implementation
is geared towards, and so it's both the simplest and the most efficient way to create it (in our case, though we
could've taken a different approach if we wanted to prioritise e.g. top-down creation).

Even though it wouldn't be the best way to do it, you could also create it top-down:
```python
tree = BinaryTree()
c = BinarySubtree(item="c")
tree.insert_root(c)
a = BinarySubtree(item="a")
c.insert_left(a)
g = BinarySubtree(item="g")
c.insert_right(g)
b = BinarySubtree(item="b")
a.insert_right(b)
e = BinarySubtree(item="e")
g.insert_left(e)
d = BinarySubtree(item="d")
e.insert_left(d)
f = BinarySubtree(item="f")
e.insert_right(f)
```

Or create all the bits individually and then link them together:
```python
tree = BinaryTree()
a = BinarySubtree(item="a")
b = BinarySubtree(item="b")
c = BinarySubtree(item="c")
d = BinarySubtree(item="d")
e = BinarySubtree(item="e")
f = BinarySubtree(item="f")
g = BinarySubtree(item="g")
a.insert_right(b)
c.insert_left(a)
e.insert_left(d)
e.insert_right(f)
g.insert_left(e)
c.insert_right(g)
tree.insert_root(c)
```

(Generally trees aren't created quite as manually as this, and are instead created iteratively or recursively through
some algorithm, for example the one in `BinaryTree.build`.)

Anyway, having created our tree (however we managed it), which again was

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

if we were to call `contains` on the various subtrees, we'd get the following results:

(To help with reading the table: for the expression `a.contains("b")`, we can look at the `a` row and the `"b"` column
and see that it should evaluate to `True`.)

| `contains` | `"a"`   | `"b"`   | `"c"`   | `"d"`   | `"e"`   | `"f"`   | `"g"`   | anything else |
|------------|---------|---------|---------|---------|---------|---------|---------|---------------|
|        `a` | `True`  | `True`  | `False` | `False` | `False` | `False` | `False` | `False`       |
|        `b` | `False` | `True`  | `False` | `False` | `False` | `False` | `False` | `False`       |
|        `c` | `True`  | `True`  | `True`  | `True`  | `True`  | `True`  | `True`  | `False`       |
|        `d` | `False` | `False` | `False` | `True`  | `False` | `False` | `False` | `False`       |
|        `e` | `False` | `False` | `False` | `True`  | `True`  | `True`  | `False` | `False`       |
|        `f` | `False` | `False` | `False` | `False` | `False` | `True`  | `False` | `False`       |
|        `g` | `False` | `False` | `False` | `True`  | `True`  | `True`  | `True`  | `False`       |

The following table gives the level, length and height of each subtree, which should be returned by `get_level`,
`get_length` (or `_calculate_length`) and `get_height` (or `_calculate_height`) respectively:

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

| Subtree | Level | Length | Height |
|---------|-------|--------|--------|
|     `a` |     1 |      2 |      1 |
|     `b` |     2 |      1 |      0 |
|     `c` |     0 |      7 |      3 |
|     `d` |     3 |      1 |      0 |
|     `e` |     2 |      3 |      1 |
|     `f` |     3 |      1 |      0 |
|     `g` |     1 |      4 |      2 |

As well as checking for membership of given items with `contains`, or getting information such as subtrees' levels, etc,
we may also want to iterate over the items in the tree, or a given subtree.

However, the order in which you may want to do this is less obvious than for a linear structure like a list. For lists,
usually you either want to iterate over the items forwards or in reverse, but there are _several_ different orders in
which people commonly iterate over - or "traverse" - binary trees.

Tree traversals are most naturally implemented recursively. Regardless of particular order, in the recursive function,
defined on a subtree, there are three things to iterate over:
- the item at the root of the subtree
- (recursively) its left subtree, if there is one
- (recursively) its right subtree, if there is one

The orders are then generally described by the order in which these are done. For example, pre-order is described as
"node, left, right" or "N L R" - but since we're talking about subtrees, we'll describe it as
"root-left-right". Either way, what that means is that the subtree's item comes first in the iteration/traversal, then
its left subtree and its descendants (in the same manner), then (similarly) its right subtree (and its descendants).

Using the tree above as an example (shown again to aid comparison), the types are:

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

Pre-order, "root-left-right":
```
c a b g e d f
=============

c
'-.---.
  a   g
  '-. '-.
    b   e
        '-.-.
          d f
```
```
a:   a b
b:     b
c: c a b g e d f
d:           d
e:         e d f
f:             f
g:       g e d f
```

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

In-order, "left-root-right":
```
a b c d e f g
=============

    c
.---'-------.
a           g
'-.     .---'
  b     e
      .-'-.
      d   f
```
```
a: a b
b:   b
c: a b c d e f g
d:       d
e:       d e f
f:           f
g:       d e f g
```

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

Post-order, "left-right-root":
```
b a d f e g c
=============

            c
  .-------.-'
  a       g
.-'     .-'
b       e
    .-.-'
    d f

```
```
a: b a
b: b
c: b a d f e g c
d:     d
e:     d f e
f:       f
g:     d f e g
```

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

Reverse pre-order, "root-right-left":
```
c g e f d a b
=============

c
'-.-------.
  g       a
  '-.     '-.
    e       b
    '-.-.
      f d
```
```
a:           a b
b:             b
c: c g e f d a b
d:         d
e:     e f d
f:       f
g:   g e f d
```

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

Reverse in-order "right-root-left":
```
g f e d c b a
=============

        c
.-------'---.
g           a
'---.     .-'
    e     b
  .-'-.
  f   d
```
```
a:           b a
b:           b
c: g f e d c b a
d:       d
e:   f e d
f:   f
g: g f e d
```

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

Reverse post-order, "right-left-root":
```
f d e g b a c
=============

            c
      .---.-'
      g   a
    .-' .-'
    e   b
.-.-'
f d
```
```
a:         b a
b:         b
c: f d e g b a c
d:   d
e: f d e
f: f
g: f d e g
```

In the above illustrations of traversals, the first block, e.g.
```
f d e g b a c
=============

            c
      .---.-'
      g   a
    .-' .-'
    e   b
.-.-'
f d
```
shows the iteration order if called on the entire tree. In this case, it shows that if you call
`tree.reverse_post_iterator()` the items are yielded in the order `f d e g b a c`. (Since we're yielding items, what's
yielded is really `f.get_item() d.get_item() e.get_item() g.get_item() b.get_item() a.get_item() c.get_item()`, i.e.
`"f" "d" "e" "g" "b" "a" "c"`, but the important thing is the traversal _order_, so we drop the `"`s for conciseness.)
Note that the first block also contains an illustration of the binary tree, but rearranged to match - and help
visualise - the traversal order.

The second block, e.g.
```
a:         b a
b:         b
c: f d e g b a c
d:   d
e: f d e
f: f
g: f d e g
```
shows which items are iterated over (and in what order) if we're instead calling the method on a particular subtree.
For example, `a.reverse_post_iterator()` yields `"b"` then `"a"`

Note that, though the order that reverse in-order traversal visits nodes in is the reverse of in-order traversal, the
same is not generally true of reverse pre- and post-order traversals. Instead, reverse post-order traversal is the
reverse of pre-order, and reverse pre-order the reverse of post-order.

Names... ¯\\\_(ツ)_/¯

Anyway, you should find that once you manage to implement one, the others should follow straightforwardly.

Now, rewinding a bit to level, length and height, you may be wondering why you're to implement `get_level`, but
`_calculate_length` and `_calculate_height` rather than `get_length` and `get_height`.

The reason why is that we're going to be computing the lengths and heights as we go, storing them in variables, and
updating them when we need to (e.g. if we call `insert_left`), but we're not going to do that for the subtrees' levels,
which we'll instead just compute when they're actually asked for (by someone calling `get_level`).

This isn't fundamental to binary trees, and is almost a subjective choice - or at least one that comes with tradeoffs
when compared to other potential approaches. We could instead have decided to compute all of them on the fly, or none of
them. Part of the point of doing it this way is that you can see both approaches (that is, either computing/recomputing
things as we go or waiting until we're asked for them). However, there is a little more logic behind it than just that.

For the length and height, the approach of having them be ready in variables that we keep updated, enabling
constant-time access, gives us more of a benefit for less of a cost than doing the same thing with the level does.

When we're creating a `BinarySubtree`, we can specify upfront the left and right subtrees (to save having to then call
`insert_left`/`insert_right`). Even if these are non-empty, though, if we can get their length/height in $\mathrm{O}(1)$
time (which we can if we're taking this approach), then we can compute the length/height of the subtree we're creating
(which is their parent) in $\mathrm{O}(1)$ time. (To calculate the subtree's length $n$, if we've already calculated
that the left subtree's length is $n_l$ and the right subtree's $n_r$, then $n = 1 + n_l + n_r$ is a constant-time
operation.)

Later, when we're running `insert_left`/`insert_right`/`remove_left`/`remove_right`, the length/height might change
(the length certainly will, the height merely might), and we'll therefore need to update our `_length`/`_height`
variables. This wouldn't necessarily be a problem, as we could again recompute them in constant time. _However_,
it's not just the subtree you're calling the `insert_*`/`remove_*` method on that's affected, but also its
ancestors. We're updating because one of our child subtrees changed, but if we change, then our parent, to whom we're a
child, will need to do the same - and if _it_ changes, then what about _its_ parent? And on and on, all the way to the
root.

The good news is that when we're updating us, then our parent, then our parent's parent, etc, for the height at least
we'll often be able to stop early before we get all the way to the root, because at some point the height won't have
actually changed. (To understand this, think about how height is calculated.) The bad news is that length changes always
propagate the whole way, up to and including the root. The other bad news is that for both of these, length _and_
height, this updating is therefore not constant time, and is instead linear in the level (because the level corresponds
to how many ancestors we have). (For height there's again the silver lining that it's $\mathrm{O}(level)$ only in the
worst case, and in the best case is $\mathrm{O}(1)$, but we're updating both of them, so the combined best case is
$\mathrm{O}(level)$.) The really bad news is that this means our `insert_*` and `remove_*` methods, which would
otherwise have been constant-time, are now linear.

That's the cost, but as we'll explain in a moment it's not necessarily such an awful cost, and we do gain relatively
well from it. The gain is, of course, that `get_length` and `get_height` can now go from linear- to constant-time. This
is especially nice because they were linear not in the subtree's level, but in its length. For leaves, or very "deep"
subtrees near the bottom of the tree, their level may be more than their length. Most subtrees, in most trees, however,
have many more descendants than they do ancestors.

This swapping of a $\mathrm{O}(length)$ `get_{length,height}` for $\mathrm{O}(level)$ `{insert,remove}_*` seems,
therefore, to be a pretty good tradeoff. Of course, whether it actually is or not depends on the use-case. For an
application that calls `{insert,remove}_*` methods loads, but never really calls `get_{length,height}`, it wouldn't be
such a great thing.

Still, it's a better tradeoff than for `get_level`. Part of the reason (apart from the fact that many more applications
need to use `get_length` heavily than `get_level`) is that it's not that bad in the first place: Computing `get_level`
takes time linear in the level! Of course, for it to be constant-time would be even better, but the cost of this
improvement is much more prohibitive than it is for length/height.

Consider again our example binary tree

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

A fairly common thing we do with trees is to rearrange them, for one reason or another. What if we wanted to move the
`g` subtree, from being the right child of `c` to being the right child of `b`?

In code, that might look like:
```python
g_subtree = c.remove_right()
b.insert_right(g_subtree)
```

Illustrated:

![(() a (b)) c ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/c_remove_right.png)

![(() a (() b (((d) e (f)) g ()))) c ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/b_insert_right.png)

Both after removing the subtree, and after reinserting it, we'd have to update all the levels (all $length$ of them - in
this case, 4). We could come up with additional "move" methods that for when we want to remove and reinsert a subtree
somewheere else, and this would mean we only have to update them all once rather than twice, but that doesn't change
the asymptotics. The cost would still be $\mathrm{O}(length)$, which (as we mentioned) is usually quite a bit more than
the $\mathrm{O}(level)$ incurred in trying to get an efficient `get_length` and/or `get_height`.

There are sure to be use-cases where this would be a worthwhile tradeoff, but (a) relatively rare ones and (b) the
important thing is the higher-level point about how trying to improve efficiencies in one place can worsen them in
another, and whether that's a good trade depends both on what aspect you're trying to improve and how you're trying to
improve it, and also what the particular application is and how often it uses different operations.

Going back to something we mentioned earlier: It's because of our "improvements" to `get_length` and `get_height` that
constructing bottom-up is more efficient than top-down - otherwise they'd be essentially equivalent. (You may be
interested to think through why this is.)

Before you start the exercise, here are a couple of quick Python tips you'll likely find useful:
- You can write `max(a, b)` to get the greater of `a` and `b`, so e.g. `max(2, 3) == 3` and `max(0, -1) == 0`.
- You can write `yield from iterator` instead of `for item in iterator: yield item`.

Good luck!
