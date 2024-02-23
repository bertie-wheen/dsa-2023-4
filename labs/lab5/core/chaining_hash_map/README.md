# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/README.md))

### [Chaining Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/chaining_hash_map/README.md)
```shell
python labs chaining_hash_map
```

In this exercise, we're implementing a hash map - again, what the lectures call a hash _table_ - using the chaining
approach, where we have an array of chains, with each chain corresponding to a particular hash value, and containing all
the mappings whose keys hash to that value. We use hashes as indices, so for example to look up a given mapping (i.e.
given a key get the corresponding value) we hash the key, treat that hash as an index, get the chain at that index, and
then search for the mapping within that chain. If it's in the map at all, it will be in that chain, and so we either
very quickly find it or, if it's not in the chain, we know that it's not in the map without having to check all the
other chains. For this to work our hash function must depend on the number of chains, as the hashes it returns must be
non-negative integers less than the chain count, in order for us to use them as indices. We're going to use the
`HashFunction` class we implemented in the previous exercise, and since that takes the range of hash values as an
initialization parameter, when we resize the hash map (for example to increase the number of chains if there are
sufficiently many items that performance is starting to degrade) we choose a new random hash function that generates
hashes within the correct range.

The `_resize` method is written for you, but (a) it uses `insert`, which is currently unimplemented, and which therefore
you'll need to implement for it to work, and (b) you need to call it in the right way at the right times. More
specifically: You'll need to call it in `insert` (don't worry, if you do it right that's not actually as circular as it
sounds, i.e. it shouldn't cause an infinite loop) when the key of the mapping to be inserted isn't already in the map,
and therefore inserting it will increment the map's length to a point where the load factor exceeds the given limit.
That limit is the "maximum load factor", chosen when creating the map. As a reminder, the load factor is
$\frac{length}{chain\_count}$ - so, if increasing the length will cause the ratio to become too large, then increasing
the number of chains can bring it back below the maximum. As with dynamic array lists, there are other amounts you might
choose to increase it by, but for the purposes of this module you should just double the chain count. Also similarly to
dynamic array lists, if `remove`-ing a mapping, and thus decrementing the length, brings the load factor down below some
point, which for our purposes we will decide is a quarter of the maximum load factor, then the array of chains should be
reallocated to halve their number (remembering that there must always be at least one chain!).

The full list of methods that you're expected to implement is:
- `contains`
- `get`
- `insert`
- `remove`

It's probably best to do them in that order, as `contains` is easier than `get`, which is easier than `insert` and
`remove`, and `insert` is needed for `_resize` which is needed for `remove`.

Good luck!

(One final note: we're using `DoublyLinkedList`s as chains, but as mentioned in the lectures chains could just as well
be any sort of list with basic operations no worse than linear time. Our choice is fairly arbitrary, and you could
choose differently if you implement your own chaining hash map outside of these labs: We use a linked list partly just
to play on the idea of a chain, what with them having links and everything... and, with slightly more reason, we choose
`DoublyLinkedList` over `SinglyLinkedList` because `DoublyLinkedNode.remove` has constant- rather than linear-time
performance, and you may find that you want to use that method in `ChainingHashMap.remove`. Incidentally, in that -
and other methods - you may well find `DoublyLinkedList.nodes_iterator` helpful.)

---

Next:
- [Probing Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/probing_hash_map/README.md)
