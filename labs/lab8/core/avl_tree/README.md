# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 8: AVL Trees](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab8/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab8/core/README.md))

### [AVL Trees](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab8/core/avl_tree/README.md)
```shell
python labs avl_tree
```

In the previous exercise we implemented a basic binary search tree. BSTs, though, like lists or maps, are a more generic
type of thing than a specific style of implementation. AVL trees, which we'll implement in this exercise, are a type of
BST. (Red-black trees are another very commonly-known and -used type.)

(AVL trees are the first data structure we've encountered whose name isn't a description of or intuition for the
structure - instead, the letters AVL come from the surnames of Georgy **A**delson-**V**elsky and Evgenii **L**andis, the
pair who came up with the idea.)

Our relatively simple BST from before had a fairly important problem: If you performed a number of insertions and
deletions on it, then depending on the order of those operations its performance could vary dramatically.

Starting from an empty tree, if you inserted `d`, then `b`, then `f`, then `a`, `c`, `e`, `g`, you'd get:

![((a) b (c)) d ((e) f (g))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/perfect_tree.png)

(And actually there are 191 other insertion orders that produce the same tree, including `d`, `f`, `e`, `b`, `c`, `a`, `g`.)

If you had instead inserted them in the order `a`, `b`, `c`, `d`, `e`, `f`, `g`, you'd get the pathological result:

![() a (() b (() c (() d (() e (() f (g))))))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/linear_tree.png)

(Note that the tree above is basically just a linked list - in a way, linked lists are just a degenerate form of trees.)

(Incidentally, there are some plants that are similarly linear.
[Here's a picture I took of one](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/linear_plant.jpg) -
I don't know the species, but there are many like it.)

Both are BSTs containing the same items, but the first you can search in $\mathrm{O}(\log(n))$ time and the second in
$\mathrm{O}(n)$. With BSTs you want breadth, not depth, as performance scales not with the number of items in the tree,
but with the height of the tree. Remember that insertion/search/removal were all $\mathrm{O}(h)$. In the worst case
(demonstrated by the latter example) these are the same, but in the best case (the former) height is instead the
logarithm of the item count.

(As these are binary trees, it is the base-2 logarithm - the minimum height of ternary trees is the base-3 logarithm of
their size, etc - but the specific base matters less than the fact that it's the logarithm. Anything logarithmic is
better than linear in the limit - similarly, we're often more concerned about whether something runs in polynomial time,
regardless of whether that's $\mathrm{O}(n^2)$ or $\mathrm{O}(n^{22})$, because for any $p$, $\mathrm{O}(n^p)$ is better
in the limit than e.g. anything exponential, such as $\mathrm{O}(2^n)$. As well as thinking of minimising height for a
given number of items, you can think about maximising item count for a given height, which is roughly the inverse, and
possibly easier to understand: bearing in mind that in level $l$ of a binary tree you can store $2^l$ items, the maximum
number of items you can fit in a binary tree of height $h$ is $2^{h + 1} - 1$, or approximately $2^h$, i.e. it scales
exponentially with height.)

(In fact it's the ["floor"](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of the base-2 logarithm. Height
can only be an integer, but logarithms rarely are. In the above example, $n = 7$ and
$\lfloor \log(n) \rfloor = \lfloor 2.8\dots \rfloor = 2$. However we either write
$\mathrm{O}(\log(n))$ or, to be more precise, $\mathrm{O}(\log_2(n))$, but don't write
$\mathrm{O}(\lfloor \log_2(n) \rfloor)$ as, like with constant factors, it makes no significant difference in the limit.)

We say that the former of the above trees is "balanced", and the latter "unbalanced".

Given an unbalanced BST, we can balance it using a pair of operations called "rotations". These operate on a
node/subtree and one or the other of its children. Often people will talk about "rotating left" or "rotating right",
but as that terminology is both strange - "left" and "right" describe directions of translational, not rotational,
motion - and ambiguous - what some people call a left rotation, others call a right rotation, and vice versa - in this
module we've decided to describe them as "clockwise" and "anticlockwise". These are better terms for talking about
rotations with, though we will explain in a moment why thinking of these operations as rotations in the first place
ought to be taken with a pinch of salt.

Here's an illustration of what these operations do - or rather, here's what is essentially the same illustration, three
times, once for when the subtree they're operating on is the root of its tree, and then twice for when it's instead a
left or right child:
```
+-------------------+                       +-------------------+
|   <   <   <   <   |                       |   <   <   <   <   |
|---+---+---+---+---|                       |---+---+---+---+---|
|   |   |   | y |   | === y.rotate_cw() ==> |   | x |   |   |   |
|   | .-------'---. |                       | .---'-------. |   |
|   | x |   |   | c | <== x.rotate_acw() == | a |   |   | y |   |
| .---'---. |   |   |                       |   |   | .---'---. |
| a |   | b |   |   |                       |   |   | b |   | c |
+-------------------+                       +-------------------+
```
```
+-----------------------+                       +-----------------------+
|   <   <   <   <   <   |                       |   <   <   <   <   <   |
|---+---+---+---+---+---|                       |---+---+---+---+---+---|
|   |   |   |   |   | p |                       |   |   |   |   |   | p |
|   |   |   | .-------' | === y.rotate_cw() ==> |   | .---------------' |
|   |   |   | y |   |   |                       |   | x |   |   |   |   |
|   | .-------'---. |   | <== x.rotate_acw() == | .---'-------. |   |   |
|   | x |   |   | c |   |                       | a |   |   | y |   |   |
| .---'---. |   |   |   |                       |   |   | .---'---. |   |
| a |   | b |   |   |   |                       |   |   | b |   | c |   |
+-----------------------+                       +-----------------------+
```
```
+-----------------------+                       +-----------------------+
|   <   <   <   <   <   |                       |   <   <   <   <   <   |
|---+---+---+---+---+---|                       |---+---+---+---+---+---|
| p |   |   |   |   |   |                       | p |   |   |   |   |   |
| '---------------. |   | === y.rotate_cw() ==> | '-------. |   |   |   |
|   |   |   |   | y |   |                       |   |   | x |   |   |   |
|   |   | .-------'---. | <== x.rotate_acw() == |   | .---'-------. |   |
|   |   | x |   |   | c |                       |   | a |   |   | y |   |
|   | .---'---. |   |   |                       |   |   |   | .---'---. |
|   | a |   | b |   |   |                       |   |   |   | b |   | c |
+-----------------------+                       +-----------------------+
```

In these illustrations, `a`, `b` and `c` are all optional - they might be `None`, or might not. Only `x` and `y` are
actually required.

We've drawn vertical dividers topped with `<`s to represent the BST condition of in-order sortedness. They also
illustrate a reason why these operations aren't _exactly_ rotations, which is that they only cause movement up and down,
and never left or right. After a rotation some subtrees change level, being either one level further up or one level
further down in the tree, but in-order iteration on the tree will yield the same items in the same order both before and
after the rotation. In fact, the fact that they'll never violate the sortedness invariant is _why_ we're able to use
these operations to rebalance BSTs.

As an example, given

![() a (() b (() c (() d (() e (() f (g))))))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/linear_tree.png)

if we ran
```python
a.rotate_acw()
c.rotate_acw()
b.rotate_acw()
e.rotate_acw()
```

we'd transform it into

![((a) b (c)) d ((e) f (g))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/perfect_tree.png)

Step-by-step:

| Operation        | Resulting tree   |
|------------------|------------------|
| `a.rotate_acw()` | ![(a) b (() c (() d (() e (() f (g)))))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/a_rotate_acw.png) |
| `c.rotate_acw()` | ![(a) b ((c) d (() e (() f (g))))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/c_rotate_acw.png) |
| `b.rotate_acw()` | ![((a) b (c)) d (() e (() f (g)))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/b_rotate_acw.png) |
| `e.rotate_acw()` | ![((a) b (c)) d ((e) f (g))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/perfect_tree.png) |

Of course, as _users_ of a BST, we don't want to have to manually run these operations. We just want something that
implements the map interface (perhaps with some conditions on the efficiencies of certain operations), we don't want to
have to worry about the internals of how the BST we're using works, and figure out which subtrees to rotate, when, and
in which direction. Even if we did, our code would be very brittle: if we changed which map operations we're calling on
the tree, we'd likely have to figure it all out anew.

What we want, then, is for the tree to handle it itself - what we want is a _self-balancing_ BST!

AVL trees are a type of self-balancing binary search tree. What that means in practice is that we, as users of an AVL
tree, can merrily call map operations on it however we like, and never suffer degradation to $\mathrm{O}(n)$
performance, as the tree will keep its height (approximately) minimal, meaning we can always e.g. search it in
$\mathrm{O}(\log(n))$ time - and it will do this without (asymptotic) slowdown to the other operations / the best case!

But how? Something to notice is that only `insert` and `remove` can cause a balanced tree to become unbalanced - and
even then, only sometimes. Additionally, even if the tree becomes unbalanced after an insertion or removal, it won't be
_that_ unbalanced. It _was_ balanced, and only one item has been inserted or removed since then, so it must still be
_nearly_ balanced. Because of this, we can then rebalance it with at most some constant amount of extra work.

Before we discuss how AVL trees do this, it's worth reminding that there are two definitions of "balanced".

The general definition, which is used to describe all kinds of binary trees, and is the property we really care about,
is that trees are "balanced" when their height is $\mathrm{O}(\log(n))$ - that is, their height is approximately*
minimal for the number of items they contain.

\* We don't necessarily want them to _always_ be _absolutely_ optimal - that would be too strong a constraint, in that
it would need too much rebalancing. Maintaining _absolute_, as opposed to _approximate_, optimality requires a massive
amount of extra work for very marginal gains. With these AVL trees, for example, some of them could be rearranged to
reduce their height by a level, but their height is always approximately $\log(n)$, which is good enough. For a tree of
$n$ items, the optimal height is $\lfloor \log_2(n) \rfloor$, and some AVL trees will instead have a height of
$\lfloor \log_2(n) \rfloor + 1$. For large $n$, $\log(n)$ vs $\log(n) + 1$ is a meaningless difference - it's $\log(n)$
vs $n$ that's the qualitative improvement.

When we're thinking about AVL trees, however, we usually have a slightly different notion of "balance", based on whether
or not, for all of the subtrees, the heights of their child subtrees differ by at most one. That is, that there's no
subtree whose children's heights differ by more than one. Though this is a different condition, AVL trees use this as a
sort of proxy for the $h = \mathrm{O}(\log(n))$ property we care about, and can do this because the AVL notion of
balance implies the general notion. (Note, though, that the reverse isn't true! There are balanced trees that contain
subtrees with children whose heights differ by more than one. The important thing is that if the AVL condition is
satisfied, then the tree will be balanced, i.e. its height will be approximately $\mathrm{O}(\log(n))$.)

The core of the AVL tree approach to staying (sufficiently) balanced is in the idea of "balance factors".
A subtree's balance factor is the signed difference between the heights of its subtrees:
```math
\mathrm{balance\_factor}(subtree) =
\mathrm{right\_height}(subtree) -
\mathrm{left\_height}(subtree)
```

AVL trees maintain the invariant that every subtree in the tree has
a balance factor in the range $[-1, +1]$, i.e. $-1$, $0$ or $+1$.

Our running example from the last couple of exercises,

![(() a (b)) c (((d) e (f)) g ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_tree/example_tree.png)

is *not* an AVL tree, as `g` has a balance factor of $(-1) - (+1) = -2$.

If we were to do `g.rotate_cw()`, however, we'd get

![(() a (b)) c ((d) e ((f) g ()))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/g_rotate_cw.png)

which is an AVL tree, as the subtrees are all in sorted order and balanced.

Using that as our example instead, here are its subtrees' balance factors:

| Subtree | Left Height | Right Height | Balance Factor     |
|--------:|------------:|-------------:|-------------------:|
| a       | $-1$        |  $0$         |  $(0) - (-1) = +1$ |
| b       | $-1$        | $-1$         | $(-1) - (-1) =  0$ |
| c       | $+1$        | $+2$         | $(+2) - (+1) = +1$ |
| d       | $-1$        | $-1$         | $(-1) - (-1) =  0$ |
| e       |  $0$        | $+1$         | $(+1) -  (0) = +1$ |
| f       | $-1$        | $-1$         | $(-1) - (-1) =  0$ |
| g       |  $0$        | $-1$         | $(-1) -  (0) = -1$ |

AVL trees use these balance factors to decide when, where and which way to rotate subtrees to rebalance themselves.

Because of this, they need $\mathrm{O}(1)$ access to them, and so they store the balance factors on the corresponding
subtrees, and update them when necessary to keep them correct. Some will instead only store the subtrees' heights, as
their balance factors can be calculated in $\mathrm{O}(1)$ if getting their child heights is $\mathrm{O}(1)$. (Some will
store _only_ the balance factors, and not the heights, but this is much harder to implement correctly.) In this
exercise, we will store both the heights _and_ the balance factors, and so the `_AVLSubtree` class has the `int` members
`_height` and `_balance_factor`.

For the most part, AVL trees implement their operations in much the same way as the simple BST of the previous lab.

However, after inserting or removing an item, some of the subtrees' heights and balance factors may have changed, so the
cached values will need to be updated, and moreover the AVL condition of all balance factors being in the range
$[-1, +1]$ may have been violated, in which case we will need to perform one or more rotations to restore our invariant
and rebalance the tree.

Let's first consider insertion.

If the given key was already in the tree, then we will have merely updated the value it's mapped to, without changing
the structure of the tree, and therefore no heights / balance factors will need changing.

Otherwise, if we are inserting a new subtree containing the given item, you should remember from before that it will
always be a leaf. (If you don't remember, go back over the previous BST material, or think it through yourself and
figure out why this is true.)

If the tree was empty, then it will also be the root, but let's not worry about this case either as, like when we're
updating an already-contained key, there's nothing much to do or say. (There can't be any other subtrees that need
their heights / balance factors recalculated, because there aren't any other subtrees!)

Now then, we come to the interesting case(s), in which we've inserted a leaf as the child of some parent.

If the parent already had a child (i.e. if it had a left child, and we've added the new leaf as its right child, or
vice versa), then that child it already had must also be a leaf, as otherwise the AVL condition wouldn't have been
satisfied, and we're maintaining the invariant that it always is (at least as a pre-condition and post-condition,
even if it may be temporarily violated within the operation itself).

In this case, the parent's balance factor will have changed from $\pm 1$ ($-1$ if it had a left child, $+1$ if it had a
right child) to $0$, so we need to update that, but the AVL condition is still satisfied. Its height, however, will be
unaffected, as the new child's height isn't greater than the old child's height (they're both 0, as they're both
leaves), and therefore the parent's height will remain as 1. Because the parent's height hasn't changed, we know that
_its_ parent's height and balance factor won't have changed (as they're calculated in terms of it), and therefore
neither will any of its other ancestors' further up towards the root.

Now we get to the most important, and complex, case. If the parent _didn't_ already have a child, then both its height
and its balance factor will need updating (its height from $0$ to $1$, and its balance factor from $0$ to $\pm 1$,
depending on which child the new leaf has been added as). Its balance factor, once updated, will still be in the right
range. _However_, as its height has changed, _its_ parent's height may have changed, and its parent's balance factor
_will_ have changed.

Crucially, the balance factor of the parent's parent (which we'll call the grandparent) may now be $-2$ or $+2$, and
therefore outside of the $[-1, +1]$ range. Here are the four ways in which this can happen (in them, the new leaf is
$n$, its parent is $p$, and its grandparent $g$):

| 1. "left-left" | 2. "left-right" | 3. "right-left" | 4. "right-right" |
|----------------|-----------------|-----------------|------------------|
| ![((n) p ()) g ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_1.png) | ![(() p (n)) g ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_2.png) | ![() g ((n) p ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_3.png) | ![() g (() p (n))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_4.png) |

We describe these cases (or rather the more general cases that these are examples of) as "left-left", "left-right",
"right-left" and "right-right", respectively. The first left/right indicates which of the grandparent's children the
parent is, and the second which of the parent's children the leaf is.

To rebalance the first, we would run `g.rotate_cw()`, for the second, we would run both `p.rotate_acw()` and then
`g.rotate_cw()`, for the third, we'd run `p.rotate_cw()` followed by `g.rotate_acw()`, and for the fourth, simply
`g.rotate_acw()`:

|             | LL | LR | RL | RR |
|------------:|:--:|:--:|:--:|:--:|
| Unbalanced: | ![((n) p ()) g ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_1.png) | ![(() p (n)) g ()](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_2.png) | ![() g ((n) p ())](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_3.png) | ![() g (() p (n))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_4.png) |
| Rebalanced: | ![(n) p (g)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/rebalanced_1.png) | ![(p) n (g)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/rebalanced_2.png) | ![(g) n (p)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/rebalanced_3.png) | ![(g) p (n)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/rebalanced_4.png) |

Even if we're not in this situation, and the grandparent's balance factor is still between $-1$ and $+1$, another
ancestor further up in the tree may have become unbalanced.

For example, _its_ parent (i.e. the great-grandparent) may have:

![((() p (n)) g ()) gg (x)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/unbalanced_5.png)

In the above example, before $n$ was added, $gg$ (the great-grandparent) had a balance factor of $-1$, but having
inserted $n$ it's now $-2$, meaning that we need to do some rebalancing.

This is another example of a "left-left" case, as $g$ is the left child of $gg$ (and $gg$ is left-heavy), and $p$ is the
left child of $g$ (and $g$ is left-heavy). Therefore, we similarly perform `gg.rotate_cw()` to get the rebalanced
(sub)tree:

![((() p (n)) g ()) gg (x)](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/avl_tree/rebalanced_5.png)

It might not be the grandparent or the great-grandparent, but instead some great-great-great-…-grandparent whose balance
factor has become $\pm 2$. Or they might all still be balanced, and just need their heights and balance factors
recalculating. Assuming, though, that there is an unbalanced ancestor, it will always locally look like one of these
four cases (we've called the unbalanced subtree $z$, its heavier child $y$, and _its_ heavier child $x$, and $p$, $a$,
$b$, $c$ and $d$ are all optional):

<table>
<tr>
<th>

"Left-Left"

</th>
<th>

"Left-Right"

</th>
<th>

"Right-Left"

</th>
<th>

"Right-Right"

</th>
</tr>
<tr>
<td>

```
          p
          |
          z
      .---'-.
      y     d
  .---'-.
  x     c
.-'-.
a   b
```

</td>
<td>

```
          p
          |
          z
  .-------'-.
  y         d
.-'---.
a     x
    .-'-.
    b   c
```

</td>
<td>

```
    p
    |
    z
  .-'-------.
  a         y
        .---'-.
        x     d
      .-'-.
      b   c
```

</td>
<td>

```
  p
  |
  z
.-'---.
a     y
    .-'---.
    b     x
        .-'-.
        c   d
```

</td>
</tr>
<tr>
<td align='center'>

`z.rotate_cw()`

</td>
<td align='center'>

`y.rotate_acw()`

</td>
<td align='center'>

`y.rotate_cw()`

</td>
<td align='center'>

`z.rotate_acw()`

</td>
</tr>
<tr>
<td>

```
      p
      |
      y
  .---'---.
  x       z
.-'-.   .-'-.
a   b   c   d
```

</td>
<td>

```
          p
          |
          z
      .---'-.
      x     d
  .---'-.
  y     c
.-'-.
a   b
```

</td>
<td>

```
  p
  |
  z
.-'---.
a     x
    .-'---.
    b     y
        .-'-.
        c   d
```

</td>
<td>

```
      p
      |
      y
  .---'---.
  z       x
.-'-.   .-'-.
a   b   c   d
```

</td>
</tr>
<tr>
<td>
</td>
<td align='center'>

`z.rotate_cw()`

</td>
<td align='center'>

`z.rotate_acw()`

</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>

```
      p
      |
      x
  .---'---.
  y       z
.-'-.   .-'-.
a   b   c   d
```

</td>
<td>

```
      p
      |
      x
  .---'---.
  z       y
.-'-.   .-'-.
a   b   c   d
```

</td>
<td>
</td>
</tr>
</table>

Note that the "left-left" and "right-right" cases require only one rotation, but "left-right" and "right-left" need
two - the first being on the unbalanced node's taller child, effectively transforming the situation into one similar to
the simpler cases.

If there is such an ancestor, we will discover it while traversing up the chain of ancestors, from the inserted leaf (or
its parent) towards the root. We go bottom-up like this, because we can then efficiently recalculate their heights and
balance factors - the further-up subtrees can calculate in terms of the already-calculated ones further down.

An important thing to note is that, if we are performing this upwards traversal after insertion, and we find an ancestor
that has become unbalanced, and rebalance it, we then need traverse no further up, as after that rebalancing the height
of the rebalanced subtree will be back to what it was before the insertion, and thus its parent/grandparent/etc will be
unaffected, and so we don't need to carry on up to recalculate their heights / balance factors (as they won't have
changed), nor do we need to check if they've become unbalanced (because they can't have).

(The reasoning behind this isn't necessarily obvious, and we're not going to give a proper proof of it, but proofs do
exist - Adelson-Velsky and Landis proved it in their famous paper. That said, it's not too hard to see why it's true,
and if you give it a little thought you might be able to figure it out yourself.)

If we've instead just removed an item, then we do need to carry on up the chain all the way to the root regardless.

Either way, traversing up to the root is no worse than $\mathrm{O}(h)$, which is the efficiency of `insert`/`remove`
anyway, so it doesn't worsen the time complexity of either operation. In fact, because it means the tree stays balanced,
it maintains $h = \mathrm{O}(\log(n))$ and therefore improves them to $\mathrm{O}(\log(n))$.

As for the exercise itself, what you're asked to do is the recalculating and rebalancing. The recalculation shouldn't be
hard, particularly after the last couple of weeks, and therefore most of the work is in implementing the rebalancing.

To implement the rebalancing, you need to figure out which of the four cases listed above you're in (if any), and then
rotate accordingly. You also need to implement the rotations! For the rotations, you mainly need to do a lot of updating
links and swapping pointers around, but once you've done that, you should recalculate the rotated parent and child's
heights and balance factors (though you should think about which subtree's you should recalculate first, and why).

You may notice that we're potentially doing more recalculation than necessary, but we're trying to focus on an
understandable implementation, not one that's been optimized into obfuscation. If you _were_ trying to write a
highly-optimized AVL tree implementation, there are some little savings here and there that you could make, but none
that would affect the asymptotics, and anyway a bigger improvement than any of them would be to not write it in Python!

One more thing: Though the methods you're asked to implement are
- `rotate_cw`
- `rotate_acw`
- `recalculate`
- `rebalance`

you should also look at and understand `update_ancestors`, and as part of that see how it's called in `insert` and
`remove`.

Right, it's time to crack open the code and have a go - good luck!
