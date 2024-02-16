# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Binary Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/binary_search/README.md)
```shell
python labs binary_search
```

As mentioned in the previous exercise, we must add to our recommendation to consult the lecture slides a note about how
this exercise's implementation will differ from the slides' pseudocode.

In the pseudocode implementation, the binary search algorithm recurses on left/right subarrays. It does this using slice
notation which, as already mentioned, we're not using. So in these labs the recursion, though similar, is slightly
different. We instead implement binary search using a helper function that takes a couple of extra parameters, denoting
the subsection of the array within which the item is to be searched for. This means that when we recurse, we can
essentially recurse on a subarray by changing these parameters. Of course, we don't want our `binary_search` function to
take these extra parameters, but we can have `binary_search(array, item)` simply call
`_binary_search_between(array, item, 0, array.get_length() - 1)`. (We could alternatively done without a helper function
by using optional keyword arguments, though that would be slightly less efficient as we'd need to re-check whether
they're `None` each time.)

Still, everything remains much the same, the main difference being in some of the indices, since in the sliced subarrays
they would be relative to `0`, whereas with the way we're doing it they're relative to `lower_index`.

Now, another illustrative example or two.

First, finding the index of `20`, which is in the given array:

```

   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  4 | 10 | 11 | 16 | 17 | 19 | 20 | 30 | 38 | 52 | 59 | 60 | 67 | 75 | 78 | 84 | 90 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
                                        '--.-'
                       .---------<---------'
.----------------------'----------------.
   0    1    2    3    4    5    6    7
+----+----+----+----+----+----+----+----+
|  4 | 10 | 11 | 16 | 17 | 19 | 20 | 30 |
+----+----+----+----+----+----+----+----+
                    '--.-'
                       '---->----.
                         .-------'------.
                            5    6    7
                         +----+----+----+
                         | 19 | 20 | 30 |
                         +----+----+----+
                              '--.-'
                                 |
                                 6
```

And now an item - `12` - that _isn't_ in the array:
```
   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|  4 | 10 | 11 | 16 | 17 | 19 | 20 | 30 | 38 | 52 | 59 | 60 | 67 | 75 | 78 | 84 | 90 |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
                                        '--.-'
                       .---------<---------'
.----------------------'----------------.
   0    1    2    3    4    5    6    7
+----+----+----+----+----+----+----+----+
|  4 | 10 | 11 | 16 | 17 | 19 | 20 | 30 |
+----+----+----+----+----+----+----+----+
                    '--.-'
             .----<----'
.------------'------.
   0    1    2    3
+----+----+----+----+
|  4 | 10 | 11 | 16 |
+----+----+----+----+
          '--.-'
             '-->-.
               .--'-.
                  3
               +----+
               | 16 |
               +----+
               '--.-'
             .--<-'
           None
```

---

Next:
- [Unsorted Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/unsorted_array_map/README.md)
