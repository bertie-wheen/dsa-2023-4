# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 4: Sorting & Array Maps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/README.md))

### [Insertion Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/insertion_sort/README.md)
```shell
python labs insertion_sort
```

Insertion sort, given the same example as we gave selection sort, runs like this:
```
+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
      ^

+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^   ^

+---+---+---+---+---+---+---+
| 1 | 9 | 4 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
          ^

+---+---+---+---+---+---+---+
| 1 | 4 | 9 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^   ^<->^

+---+---+---+---+---+---+---+
| 1 | 4 | 9 | 3 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
              ^

+---+---+---+---+---+---+---+
| 1 | 3 | 4 | 9 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^   ^<->^<->^

+---+---+---+---+---+---+---+
| 1 | 3 | 4 | 9 | 2 | 0 | 6 |
+---+---+---+---+---+---+---+
                  ^

+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 9 | 0 | 6 |
+---+---+---+---+---+---+---+
  ^   ^<->^<->^<->^

+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 9 | 0 | 6 |
+---+---+---+---+---+---+---+
                      ^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
  ^<->^<->^<->^<->^<->^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 9 | 6 |
+---+---+---+---+---+---+---+
                          ^

+---+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 6 | 9 |
+---+---+---+---+---+---+---+
                  ^   ^<->^
```

Again, you'll likely want to have a look at the lecture slides while implementing the exercise. Speaking of which, open
up `exercise.py`, and try to figure it out! (Note that, though they contain pseudocode, you shouldn't just mindlessly
transcribe it. These labs aren't marked anyway, so you'd only be cheating yourself. The point is that, even if you do
essentially just convert the pseudocode to Python, you should have your brain switched on while you do, and in the
process get to better understand how the algorithm works.)

---

Next:
- [Merge Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab4/core/merge_sort/README.md)
