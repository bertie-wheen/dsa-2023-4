# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Merge Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/merge_sort/README.md)
```shell
python labs merge_sort
```

Merge sort breaks our example down like this:
```
+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^---^---^   ^---^---^---^
  ^   ^---^   ^---^   ^---^
      ^   ^   ^   ^   ^   ^
```

And it runs like this:
```
     +---+---+---+---+---+---+---+
     | 1 | 9 | 4 | 3 | 2 | 0 | 6 |
     +---+---+---+---+---+---+---+
     '-----.-----'-------.-------'
       .---'             '---.
 .-----'-----.       .-------'-------.
 +---+---+---+       +---+---+---+---+
 | 1 | 9 | 4 |       | 3 | 2 | 0 | 6 |
 +---+---+---+       +---+---+---+---+
 '-.-'---.---'       '---.---'---.---'
  .'     '-.           .-'       '-.
.-'-.  .---'---.   .---'---.   .---'---.
+---+  +---+---+   +---+---+   +---+---+
| 1 |  | 9 | 4 |   | 3 | 2 |   | 0 | 6 |
+---+  +---+---+   +---+---+   +---+---+
'-.-'  '-.-'-.-'   '-.-'-.-'   '-.-'-.-'
  |     .'   '.     .'   '.     .'   '.
.-'-. .-'-. .-'-. .-'-. .-'-. .-'-. .-'-.
+---+ +---+ +---+ +---+ +---+ +---+ +---+
| 1 | | 9 | | 4 | | 3 | | 2 | | 0 | | 6 |
+---+ +---+ +---+ +---+ +---+ +---+ +---+
'-.-' '-.-' '-.-' '-.-' '-.-' '-.-' '-.-'
  |     '.   .'     '.   .'     '.   .'
.-'-.  .-'-.-'-.   .-'-.-'-.   .-'-.-'-.
+---+  +---+---+   +---+---+   +---+---+
| 1 |  | 4 | 9 |   | 2 | 3 |   | 0 | 6 |
+---+  +---+---+   +---+---+   +---+---+
'-.-'  '---.---'   '---.---'   '---.---'
  '.     .-'           '-.       .-'
 .-'-.---'---.       .---'---.---'---.
 +---+---+---+       +---+---+---+---+
 | 1 | 4 | 9 |       | 0 | 2 | 3 | 6 |
 +---+---+---+       +---+---+---+---+
 '-----.-----'       '-------.-------'
       '---.             .---'
     .-----'-----.-------'-------.
     +---+---+---+---+---+---+---+
     | 0 | 1 | 2 | 3 | 4 | 6 | 9 |
     +---+---+---+---+---+---+---+
```

With this exercise, you are again encouraged to consult the lecture slides (available on Canvas) for a description of
the general algorithm. However, this time we must add a little note, which isn't too important for this exercise, but
will matter in the next one, and so we make a first mention of it here.

In the pseudocode, the slides use "slice" notation for denoting subarrays. Though Python supports slice notation, many -
even most - languages don't, and so we have chosen to not use it in these labs. Therefore, when it says to e.g. "copy
`A[0 ... (m - 1)]` to `L`", you will have to iterate over the indices `i` from `0` up to `m - 1` and copy each `A[i]` in
turn.

(The following note isn't required reading, and is just because you might find it interesting. If you're uninterested
in such things, feel free to start the exercise now!)

In this exercise, merge sort - a "divide and conquer" algorithm - recursively divides up the array all the way down to
1-item chunks. This is how "pure"* merge sort works, but often in the real world it (and other divide-and-conquer
algorithms such as quicksort) stop dividing when the chunks still contain several items, and run a different algorithm
(often insertion sort) to sort these small subarrays, before unwinding the recursive call stack and merging the sorted
chunks back together. (Specifically, this approach - called tiled merge sort - stops when the chunks are small enough to
fit in the cache.) Though again: in this exercise, we go to `n = 1`, where chunks are trivially sorted, and merge back
from there.

\* (If you're a functional programmer: not pure as in a pure function, but pure as in unalloyed.)

---

Next:
- [Binary Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/binary_search/README.md)
