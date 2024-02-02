# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md) ([Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/README.md))

### [Character Generators](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/character_generator/README.md)
```shell
python labs character_generator
```

This, like the logger, is another example of a way in which we might use lists.

(Technically this application doesn't require full ordered lists, and could manage with unordered sets, but lists are
very commonly used in situations when they're arguably not the best possible choice of data structure, simply because
they're used so often and are so often usable and "good enough". It's probably wrong to admit to this in a DSA course,
but this is the applied part of the module, and you'll find many people's default reaction, if they need a collection of
items, is to reach for a list - to only use something more advanced/structured/powerful if a list would be wildly too
awkward or inefficient, and not to use simpler data structures if lists are overkill. Now, though we must frown, shake
our heads, and generally make disapproving noises about this approach, it can be somewhat justified for prototyping.
Perhaps lists are a bit like Python: Great for knocking something together quickly, but if you care about efficiency
it's probably worth redoing it using something else. And - all that said - there are many cases when lists are absolutely
the right data structure to be using!)

What this is is a set of generator functions that might be helpful for creating a character in an MMORPG / DnD
campaign / fantasy novel / etc. The main function is `generate_name`, which takes a character's sex (male/female) -
which can also be randomly chosen using `generate_sex` - and generates names such as:
- Freya Halfbear
- Count Sigurd Stormhorn
- Rune Rawbelly
- Queen Helga Ironhill
- Baroness Ingvild Ironback

It does this by storing lists of things like titles, names and their components, and then randomly choosing items from
each, which it combines to form a full name. It's far from the most sophisticated name generator, but again, that's not
really the point.

The point is to think about what operations it uses, and how, and based on that decide which type of list would be most
appropriate. Although it's storing these things in lists, the only list operation it's really using is `get_at`. We
mentioned "random access" in the `static_array_list` exercise, and it's worth noting that random access doesn't always
mean _actually random_ access, but rather effectively/potentially random, i.e. items might be accessed in any order,
without any particular pattern that might improve performance. As Wikipedia explains: "Random access (more precisely and
more generally called direct access) is the ability to access an arbitrary element of a sequence in equal time or any
datum from a population of addressable elements roughly as easily and efficiently as any other, no matter how many
elements may be in the set. In computer science it is typically contrasted to sequential access which requires data to
be retrieved in the order it was stored." This, however, is an example of genuinely-random random access (or, well,
pseudorandom random access, at least), in that whenever it calls `get_at` it generates a (pseudo)random index to call it
with.

Linked lists are great at sequential access, in that they can access their $n$ items in $\mathrm{O}(n)$, if they access
them in sequential order. However, the same can't be said about how they do with random access: if their $n$ items are
to be accessed in any given order (not just sequentially), that is instead $\mathrm{O}(n^2)$.

This is because their `get_at` operation is $\mathrm{O}(n)$. You will hopefully remember that for arrays - and thus our
`StaticArrayList` class - `get_at` is $\mathrm{O}(1)$. Therefore, given that that's the operation we care about, what
likely makes the most sense to use in this context is `StaticArrayList`.

Now, `get_at` might not actually be the _only_ operation it uses, as the lists could be dynamically added to with more
names etc, which would mean using one of the `insert_` operations, probably `insert_last`. However, there could well be
fewer of these insertions than the number of times that `get_at` is called. (Say you were to expose the application over
the internet as on online tool, for people to generate names with, but you wanted to add some extra titles first.
Assuming the tool had some success - and if not, $n$ will be smalll enough that it doesn't matter - then the number of
insertions of additional titles would be far fewer than the number of generations and thus `get_at`s. This means that
we would rather have `StaticArrayList`'s $\mathrm{O}(n)$ `insert_last` and have its $\mathrm{O}(1)$ `get_at`, rather
than a linked list's $\mathrm{O}(1)$ `insert_last` but $\mathrm{O}(n)$ `get_at`. It's worth noting too that it's not
just about the relative _number_ of these operations, but also about _when_ they're invoked. Even if you were adding
very many titles and name components, this would likely be done up front, when the amount of time that takes matters
less, whereas the `get_at` operations would be happening when a user requests a name, and when the time taken to
respond with that name matters more. Incidentally, there is a trick to get the best of both worlds in situations like
this when the operations aren't randomly interspersed, but rather their relative frequencies vary across different
phases of the application. In this context, there's a "setting-up" phase when the only operation being used is
`insert_last`, and then there's a "running" phase when it's only `get_at`. What you can do is use different data
structures at different points in the program: In the setting-up phase, you could use e.g. `SinglyLinkedList` to add
the $n$ extra components in $\mathrm{O}(n)$, then convert from `SinglyLinkedList` to `StaticArrayList` in
$\mathrm{O}(n)$ (by using `StaticArrayList.build(singly_linked_list.iterator())`) ahead of the program's running state.

Okay, that's all for this lab! In the next one we'll implement different list structures that would tick both boxes
of the above requirements quite well, and with which we needn't necessarily worry about using one data structure in
one phase and then converting to another for another, as it can do both operations in constant time!
