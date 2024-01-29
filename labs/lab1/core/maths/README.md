# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 1: Getting Ready](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/README.md))

### [Maths](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/maths/README.md)
```shell
python labs maths
```

This first exercise includes some simple functions.

In this module, the data structures will be implemented as classes, with operations as methods, and the algorithms as
functions like these. You will be implementing more data structures than algorithms, and the algorithms won't be until
later weeks, but because you should really understand functions before understanding methods, we look at these first.

If you look at a given function, say
```python
def divides(divisor: int, number: int) -> bool:
    """
    Check if the given divisor divides the given number.

    +--------+------+
    | Time:  | O(1) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter divisor: the divisor
    :parameter number: the number
    :returns: ``True`` if ``divisor`` | ``number``, else ``False``
    :raises ZeroDivisionError: if ``divisor == 0``
    """
    return number % divisor == 0
```
you will notice that it comes with a docstring explaining what the function does, and how it behaves. Most of it is
fairly normal, except for the inclusion of its worst-case time and space efficiency. (There's more on this "Big-O"
notation, which is very important to familiarise yourself with, in this week's lectures.) One thing that might look
different to Python you've seen before is the inclusion of type hints.

These are type hints:
```
def divides(divisor: int, number: int) -> bool:
                   ^^^^^        ^^^^^ ^^^^^^^^
                     1            2       3
```

These document what the types of the values given as arguments and the value returned from the function are expected to
be. _However_, this is pure annotation, with no runtime effect: If you're used to statically- (or even gradually-) typed
languages, you might expect there to be some automatic typechecking done, but no - this is still Python, and Python is
resolutely a dynamically-typed language. What this means is that the line is semantically the same as
```
def divides(divisor, number):
```
and that users of the `divides` function can pass any type of values to it (not just `int`egers), and that if we as its
implementors make a mistake (and our static analysis tools don't catch it) then something other than a `bool`ean might
be returned from it.

You might think that perhaps we should add
```python
if type(divisor) is not int:
    raise TypeError
if type(number) is not int:
    raise TypeError
```
or
```python
if not isinstance(divisor, int):
    raise TypeError
if not isinstance(number, int):
    raise TypeError
```
but for the sake of simplicity, we won't - despite this, though, we will assume that the arguments to a function/method
are of the right type (i.e. in this case that both `divisor` and `number` are `int`s). We will, however, sometimes check
their values. If the `%` operator didn't do it for us (which it does), this function would start with
```python
if divisor == 0:
    raise ZeroDivisionError
```

Probably the most advanced concept in this exercise is that of iterators.

To be honest, we're going to tell a couple of little lies about them, as we don't want to have to explain generators,
iterables, magic methods etc (though you are of course free to research those if you particularly want to get into
Python). Like Physics teachers lying about particles, this is because what we will tell you is a good enough model to
work with, and avoids having to dive straight into quantum physics. (It's not that the fuller, more accurate picture
isn't interesting or useful, but it would be too much to explain right now.)

You define an iterator like this:
```python
def divisors(number: int) -> Iterator[int]:
    """
    Get an iterator over the divisors of the given number.

    +--------+-----------+
    | Time:  | O(number) |
    +--------+-----------+
    | Space: | O(1)      |
    +--------+-----------+

    :parameter number: the number whose divisors are to be iterated over
    :returns: the divisors of ``number`` (from ``1`` to ``number``, inclusive)
    """
    for divisor in range(1, number + 1):
        if divides(divisor, number):
            yield divisor
```

In place of `return`, you write `yield`. the difference being that `return` stops execution of the function, but `yield`
merely pauses it - and as a result, can be used to return multiple values (one at a time).

We can pass an iterator to `for` to iterate over its values, like this:
```python
def divisor_count(number: int) -> int:
    """
    Get the number of divisors the given number has.

    +--------+-----------+
    | Time:  | O(number) |
    +--------+-----------+
    | Space: | O(1)      |
    +--------+-----------+

    :parameter number: the number whose divisors are to be counted
    :returns: the number of divisors of ``number`` (from ``1`` to ``number``, inclusive)
    """
    count = 0
    for divisor in divisors(number):
        count += 1
    return count
```

Even though we're not going into them too deeply, it might be worth sketching the order of execution.

The first thing that happens is that `divisors(number)` is evaluated to get the iterator. That is, the above is the same
as writing
```python
def divisor_count(number: int) -> int:
    """
    Get the number of divisors the given number has.

    +--------+-----------+
    | Time:  | O(number) |
    +--------+-----------+
    | Space: | O(1)      |
    +--------+-----------+

    :parameter number: the number whose divisors are to be counted
    :returns: the number of divisors of ``number`` (from ``1`` to ``number``, inclusive)
    """
    count = 0
    divisors_iterator = divisors(number)
    for divisor in divisors_iterator:
        count += 1
    return count
```

The `for` loop then runs the iterator until the first `yield`, at which point the value `yield`ed is assigned to the
variable `divisor`. In this case we're not actually using this value, as we're just counting divisors, without worrying
about what they are, but if we were instead summing them, instead of `count += 1` we might have written
`divisor_sum += divisor`. After `count += 1`, the `for` loop resumes the divisors iterator, which runs until the next
divisor is `yield`ed, which is again assigned to `divisor` and the loop body (`count += 1`) is re-run. This happens
repeatedly until there are no more `yield`s and the iterator stops, at which point the loop exits and the `count` is
returned.

(Incidentally, if you're a Pythonista wondering why we wouldn't use e.g. `sum`, it's because - with a few, but very few
exceptions, like `range` - we're not using built-in functions in general.)

In this exercise there's just one function for you to implement, and that is `is_even(number: int) -> bool`.
Where it says `raise NotImplementedError`, you're to replace that with an implementation (which in this case
is likely to only be one line).

Before you do that, though, go back to your terminal (or re-open it and re-`cd dsa` if you closed it), and run
```shell
python labs maths
```

If you do (and everything's setup and working correctly), you should see two failed test results.
These are for the tests `even_number_is_even` and `odd_number_is_not_even`.
The first tries to pass `is_even` some even numbers, and checks that it returns `True`,
and similarly the second passes `is_even` some odd numbers, and checks that it returns `False`.
Currently they're failing because the function fails to return anything at all, and instead raises the exception
`NotImplementedError`.

Now, quit the tests viewer (there's a `Quit` button, or press `Q` or `Ctrl-C`), and try replacing
`raise NotImplementedError` with `return True`, and re-run `python labs maths`. (Note that you can just press `Up` then
`Enter` to re-run the last command.) You should see that the `even_number_is_even` test is now passing (indicated by it
being green rather than red, and not being followed by a reason for failure), but that (unsurprisingly) the
`odd_number_is_not_even` test is still failing (though this time for a different reason).

Once you've figured out what the correct thing to write is, and both tests are passing, move on the next exercise,
featuring a class.

---

Next:
- [Players](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/player/README.md)
