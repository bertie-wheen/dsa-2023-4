# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Selection Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/selection_sort/README.md)
```shell
python labs selection_sort
```

First up: selection sort.

Before we discuss it, it's worth talking a little about the style in which we're implementing these sorting algorithms.

You'll notice that the function `selection_sort`'s signature is:
```python
def selection_sort(array: Array[Item]) -> None:
```

It could return the array, but we choose not to do that in these labs to make the point that it mutates the array it's
given, and to distinguish it from another - equivalent, but different - approach of instead returning a sorted version
of the array and leaving the one given unchanged.

There are advantages and disadvantages to each, some objective, and some subjective, but given either style you can
implement the other. For example, we could write:
```python
def selection_sorted(array: Array[Item]) -> Array[Item]:
    sorted_array = Array.build(array.iterator())
    selection_sort(sorted_array)
    return sorted_array
```

Or, given `selection_sorted`:
```python
def selection_sort(array: Array[Item]) -> None:
    sorted_array = selection_sorted(array)
    for index in range(array.get_length()):
        item = sorted_array.get_at(index)
        array.set_at(index, item)
```

(In fact, in the `merge_sort` exercise the implementation will internally be something like the latter, because merge
sort - unlike selection sort or insertion sort - lends itself most naturally to the immutable, "return sorted" style
rather than the mutating "sort". That said, it is possible to implement it using direct mutation of the original array,
and - though we don't make that an exercise - you may like to figure out how.)

(The only real efficiency difference is that if you implement `*_sort` using `*_sorted`, it requires `O(n)` auxiliary
storage, which algorithms like selection sort don't otherwise require.)

Also, for this and the next exercise you're provided a `_swap` function that, given an array and two indices into it,
swaps the items at those indices. This is because it isn't the interesting part, and also because the way we're writing
these exercises it ends up being somewhat verbose. (Note that, in "normal" Python, using e.g. the `list` type, you can
write things like `a[i], a[j] = a[j], a[i]`. You can't do that in every language though, and in those cases will have to
use at least one temporary variable, e.g. `t = a[i]; a[i] = a[j]; a[j] = t`.)

Now: selection sort. We're not actually going to talk much about these sorting algorithms in these labs, but for each we
will provide an illustrative example that you may find useful to consider while going back over the lecture slides (which
you can find on Canvas).

Specifically, for each of them, the ASCII art will represent how, given the array
```
+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
```
they sort it into
```
+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 6 | 9 |
+---+---+---+---+---+---+---+
```

Here's how selection sort does it:
```
+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^   '---'---'---'---^---'

+---+---+---+---+---+---+---+
| 0 | 9 | 4 | 3 | 2 | 1 | 6 |
+---+---+---+---+---+---+---+
  ^<----------------->^

+---+---+---+---+---+---+---+
| 0 | 9 | 4 | 3 | 2 | 1 | 6 |
+---+---+---+---+---+---+---+
      ^   '---'---'---^---'

+---+---+---+---+---+---+---+
| 0 | 1 | 4 | 3 | 2 | 9 | 6 |
+---+---+---+---+---+---+---+
      ^<------------->^

+---+---+---+---+---+---+---+
| 0 | 1 | 4 | 3 | 2 | 9 | 6 |
+---+---+---+---+---+---+---+
          ^   '---^---'---'

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
          ^<----->^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
              ^   ^---'---'

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
                  ^   '---^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
                      ^   ^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 6 | 9 |
+---+---+---+---+---+---+---+
                      ^<->^
```

If you haven't already: download the lecture slides from Canvas, open both them and `exercise.py`, and have a go
implementing `selection_sort`!

---

Next:
- [Insertion Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/insertion_sort/README.md)
