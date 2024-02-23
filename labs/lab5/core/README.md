# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/README.md))
```shell
python labs 5
```

This lab is about hashing, and particularly about how to use hashing to implement efficient maps.

Before we get into the specifics, a note about terminology:

Where the lectures talked about hash tables, these labs talk about hash maps. For most people, the two terms are
synonymous, though there is a slightly different (but very much related, and actually equivalent) structure that some
people instead mean when they say "hash table" (which uses hashing to store data for efficient retrieval in much the
same way as hash maps do - the difference being that it stores any sort of data, not just keyed data).

When discussing the theoretical aspects, and even in common parlance, what we here call hash maps are often called hash
tables. The reason we call them hash _maps_ is (a) to make it obvious that they're hash-based implementations of the map
interface, (b) to have the naming scheme be consistent with earlier data structures (e.g. `SinglyLinkedList`), where the
interface (e.g. `List`) is the last component of the name, with preceding components being increasingly more specific
about how the type implements that interface, and (c) because often in languages' standard libraries you will find types
called things like `HashMap`.

1. [Hash Functions](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/hash_function/README.md)
2. [Chaining Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/chaining_hash_map/README.md)
3. [Probing Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/probing_hash_map/README.md)
