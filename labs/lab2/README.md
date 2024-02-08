# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 2: Lists](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab2/README.md)
```shell
python labs 2*
```

If you haven't gone through [lab 1](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md),
then make sure to read through what it says about getting your system ready for working on these labs. As a reminder, if
you're on a lab machine you'll need to first:
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
- Open PyCharm and:
  - Open the `labs/` directory (i.e. `N:/dsa/labs/`) as a project
  - Switch the scope to "Exercises & Solutions" or "Exercises, Solutions & Notes" by clicking on the word "Project"
    above the directory tree in the left sidebar

There's a great setup guide (thanks to Joshua Kybett) about all of this (with screenshots and extra tips) available on
Canvas, which is worth a read-through (particularly if you don't understand a step or are having problems). There's
also a Mac-specific guide on Canvas for those of you who need it (thanks to Val Knight).

---

Another little reminder from lab 1:

Sometimes, you may want to not just run the test suite, but load the file you're working on into the Python REPL and
play around with it. To do this, first open PyCharm's Python Console, which you can do by going to the top menu and
selecting `Tools -> Python or Debug Console`, or by clicking the little Python icon in the bottom-left (that is, towards
the bottom of the left bar). Then run e.g. `from lab2.core.singly_linked_list.exercise import *` (changing the lab
number and exercise name to whatever you're working on), after which you'll be able to run things like
```pycon
>>> list = SinglyLinkedlist()
>>> list.get_length()
0
>>> list.insert_last("a")
>>> list.insert_last("b")
>>> list.insert_last("c")
>>> for item in list.iterator():
...     print(item)
...
a
b
c
>>> list.get_length()
3
```

---

One more quick reminder before starting this second lab: you are expected to do the core exercises, but if, having done
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
