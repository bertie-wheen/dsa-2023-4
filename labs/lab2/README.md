# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md)
```shell
python labs 2*
```

If you haven't gone through [lab 1](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md),
then make sure to read through what it says about getting your system ready for working on these labs. As a reminder, if
you're an a lab machine you'll need to first:
- Open the Software Hub and launch:
  - Python 3.11.3
  - PyCharm Community Edition
  - Git for Windows
- Open PowerShell and run:
  - `pip install textual`
  - If you haven't cloned this repository before, then:
    - `cd N:/`
    - `git clone https://github.com/bertie-wheen/dsa-2023-4 dsa`
    - `cd dsa`
  - If you have, then:
    - `cd N:/dsa`
    - `git pull`
    - If you get an error "fatal: detected dubious ownership in repository ..." (which you likely will),
      then run the command it recommends, which is:
      - `git config --global --add safe.directory '%(prefix)///smbhome.uscs.susx.ac.uk/<username>/dsa'`
        (where `<username>` is your username)
      - Then again run `git pull`

There's a great setup guide (thanks to Joshua Kybett) about all of this (with screenshots and extra tips) available on
Canvas, which is worth a read-through (particularly if you don't understand a step or are having problems).

---

Another quick reminder before starting this second lab: you are expected to do the core exercises, but if, having done
them, you find that you'd be up for a little extra, there are optional "plus" exercises that you might like to have a
look/go at. They're not actually harder, at least usually - admittedly there are one or two Python features that they
use (particularly `Enum`s and `match` statements) that the core exercises don't, but the point of them is interest and
general knowledge, not to be crazy hardcore. This lab's plus exercises are especially simple, to the point of not even
being exercises: Their implementations are already complete, and they are just basic examples to show when you might use
one type of list over another.

- [Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/core/README.md)
  - Singly-linked Lists
  - Doubly-linked Lists
  - Static Array Lists
- [Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/plus/README.md)
  - Loggers
  - Character Generators
