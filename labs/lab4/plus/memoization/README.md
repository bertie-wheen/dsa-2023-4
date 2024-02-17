# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/plus/README.md))

### [Memoization](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/plus/memoization/README.md)
```shell
python labs memoization
```

A common optimisation technique is called "memoization". The idea is to cache the results of a computation so that next
time they can simply be looked up rather than recomputed. The tradeoff is between space and time: memoization causes
increased memory usage, but can also dramatically improve performance.

In this example, we show two implementations of a function for getting the $n$th number in the
[Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence).

The first, `slow_fibonacci`, is the "naive" implementation. Its performance is exponential, i.e. $\mathrm{O}(2^n)$.
(Actually - and we're not going to explain _why_ this is, but it's a fun thing to note - for this function it's more
specifically $\mathrm{O}(\phi^n)$, where $\phi = 1.618\dots$ is the
[golden ratio](https://en.wikipedia.org/wiki/Golden_ratio).)

The second, `fast_fibonacci`, is a memoized version of the first. All it does differently is to store the results in a
map (`_cache`), and reuse those to avoid unnecessary recalculation. However, this change improves its time efficiency to
$\mathrm{O}(n)$, i.e. linear from exponential - or even $\mathrm{O}(1)$ for numbers it has already calculated.

Or rather it would if our map were slightly more efficient. Were we using the sort of map we'll implement in the next
lab, then it would be linear/constant, but using `SortedArrayMap` it's instead $\mathrm{O}(n \log_2(n))$ for new numbers
and $\mathrm{O}(\log_2(n))$ for those it has already calculated.

(The downside is that the memory usage, which was $\mathrm{O}(1)$ before, now grows without bound. A technique to
mitigate this is to set a maximum size for the cache, and start removing some of the cached results once it exceeds that
limit.)
