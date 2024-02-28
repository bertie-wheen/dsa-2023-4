# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 5: Hash Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/README.md)
```shell
python labs 5*
```

Welcome to lab 5! First things first: If you haven't gone through
[lab 1](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md), then make sure to read through
what it says about getting your system ready for working on these labs. As a reminder, if you're on a lab machine you'll
need to first:
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
the bottom of the left bar). Then run e.g. `from lab5.core.chaining_hash_map.exercise import *` (changing the lab number
and exercise name to whatever you're working on), after which you'll be able to run things like
```pycon
>>> map = ChainingHashMap()
>>> map.get_length()
0
>>> map.insert("c", 2)
>>> map.insert("a", 1)
>>> map.insert("c", 3)
>>> map.insert("d", 2)
>>> map.insert("b", 3)
>>> for tile, points in map.iterator():
...     print(f"'{tile}' is worth {points} point{'' if points == 1 else 's'}")
...
'a' is worth 1 point
'b' is worth 3 points
'c' is worth 3 points
'd' is worth 2 points
>>> map.get_length()
4
```

---

- [Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/core/README.md)
  - Hash Functions
  - Chaining Hash Maps
  - Probing Hash Maps
- [Plus](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab5/plus/README.md)
  - Entity-Component-System
  - Linkers
