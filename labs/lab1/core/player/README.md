# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 1: Getting Ready](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/README.md))

### [Players](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/player/README.md)
```shell
python labs player
```

This exercise introduces a `Player` class, that might be used in a simple game.

A player - which would be represented by an instance of this class - has an amount of xp (experience points), and a
position within the game world. The position is represented by a pair of integers, implying that the player is probably
moving around on some sort of 2-dimensional grid.

An example of its usage:
```python
player = Player(position=(4, 2))
player.move(2, 0)
gained_level = player.gain(1400)
if gained_level:
    print("level up!")
```

The main thing to note is that in this - and all the classes in these labs - the members are not made public. This is
done by prefixing them with underscores (`_xp` and `_position` rather than `xp` and `position`), as this is the standard
Python convention for indicating that something isn't "public", meaning that external users of the class shouldn't
access/modify them directly:

["A name prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API
(whether it is a function, a method or a data member).
It should be considered an implementation detail and subject to change without notice."](https://docs.python.org/3/tutorial/classes.html#private-variables)

The expectation, then, is that users will only interact with the class through its public methods. By restricting this
interface, we can better maintain invariants and ensure correctness.

For example, consider the player's XP. The initializer checks that it doesn't start off negative, and the `gain` method
does a similar check that the amount gained is positive, and if these are the only way the XP is accessed and modified,
then we know that it can never be negative. If there was instead a public `xp` member, users could do `player.xp = -1`
or something like that. This might not seem like a big deal, but in other situations it's crucial to maintain validity.
There will be data structures whose operations rely on the internal state not being messed up, or generally modified by
anyone "outside" of the class. The point is that if they are the only ones that directly modify the state of their
members, and they do so correctly, then it will always remain correct, and they can assume that. This assumption can
enable some significant efficiency gains.

We will have members be private even when none of the above applies for the sake of consistency.
(And, if you're experienced with Python, we're using normal getter/setter methods rather than properties to reduce
both the number of Python features required, and the number of more Python-specific features used. More and more
languages support properties, but there are still many that don't.)

There are a couple of simple methods for you to implement: `Player.get_xp` and `Player.get_y`, the point of them being
mainly to get you used to running the testing system.

If you run `python labs player`, you'll see some test failures that should turn green when you implement the methods.

If you instead run `python labs 1`, you'll see all the test results of these lab 1 core exercises.

It would be `python labs 1+` for the plus exercises, but there aren't any this lab.

There's also `python labs 1*` to show all the lab's exercises (which in this case is much the same as `python labs 1`,
as there aren't any plus exercises).

You can additionally select items in the sidebar to run the corresponding tests.

Once you've got all greens for this `player` exercise, there's only one more exercise to do this lab.

---

Next:
- [Pairs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/pair/README.md)
