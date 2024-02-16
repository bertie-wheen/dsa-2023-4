# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Sorted Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/sorted_array_map/README.md)
```shell
python labs sorted_array_map
```

In this exercise, we'll again implement the map interface by internally using an array list.

However, this time we will maintain the invariant that that list is sorted, i.e. its items are all in increasing order.
This will enable us to improve the efficiencies of the map operations, from generally linear to generally logarithmic.
This is because we can use binary search to know where a given mapping will be within the array list, assuming that it
is actually there. If it's not, then we can know that without having checked all (or even most) of the mappings.

The methods for you to implement are again:
- `insert`
- `remove`

We won't say much else, other than that you should use binary search, as to say much more would remove the challenge
from the exercise. The one thing we will say is that you shouldn't use the actual `binary_search` implementation
from the `binary_searach` exercise, but should re-implement it (perhaps with slightly different base/final cases,
and/or accumulating/maintaining additional information in the process). (If the `binary_search` implementation had
been slightly more general, and/or if we were using Python slightly differently, then you could have reused that code.
In the real world that would potentially be a good idea, but for our purposes, doing it this way is good exercise!)
