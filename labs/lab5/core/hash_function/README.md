# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/README.md))

### [Hash Functions](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/hash_function/README.md)
```shell
python labs hash_function
```

In this exercise, we implement the family of hash functions described in the lectures as universal. That is, the family

$H = \{h_{a,b} \ |\  a, b \in \{0, \dots p - 1\} \text{ with } a \ne 0\}$

where

$h_{a,b}(k) = ((a k + b \mod p) \mod N)$

An instance of the `HashFunction` class is then a specific $h_{a,b}$. As in the lectures, we pick hash function at random from the family by randomly choosing the $a$ and $b$ parameters. The instance generates these upon creation, and stores them in `self._a` and `self._b` member variables.

It has a `hash` method that can be called (e.g. `hash_function.hash(thing)`) to return (essentially) $h_{a,b}(thing)$. More accurately, it returns $h_{a,b}(to\_int(thing))$, where `to_int` is a function that converts any input to an integer. (Specifically, to a non-negative integer less than $2^{64}$.) The `hash` method accepts any sort of key, not just integers, to enable our hash maps to be generic and accept e.g. strings as keys. It first converts the thing to be hashed (for our usecases, this will a key) to an integer using `to_int` (which is provided for you, and which you shouldn't worry about the implementation of - consider a black box). It then hashes that integer using the above approach - that is, to first multiply by $a$, then add $b$, then mod $p$, then mod $N$.

We've fixed $p$ to be the prime $2^{100} - 1$, but this is somewhat arbitrary. All that's required is that it's large enough, and given that the integers will be less than $2^{64}$, any prime greater than that will do the trick. We also take $N$ (which we call `size`) as a parameter at initialisation time.

What you're to do is to implement the `hash` method, which you should do by using first `to_int`, then the given formula:

$h_{a,b}(k) = ((a k + b \mod p) \mod N)$

Note: This exercise is used in the other two exercises. So, if you've spent a while failing to figure it out, and want to have a go at them, just implement it using `return to_int(thing) % self._size` for now and come back to it later.

Still, have a go!

---

Next:
- [Chaining Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/chaining_hash_map/README.md)
