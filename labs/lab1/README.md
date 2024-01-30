# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 1: Getting Ready](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/README.md)

```shell
python labs 1*
```

(The command above will make sense soon enough.)

This module's lab exercises are written in Python. In fact, they are written in a fairly simple subset of it.
Fundamentally, this module is Data Structures & Algorithms, not Advanced Python. We want its content to be accessible
to all students, regardless of their level of prior experience with Python or programming in general. We also want the
implementations to easily translate to other languages, and therefore we not only avoid using various features because
they'd add unnecessary prerequisites, but because not every language has those features. As a result, however, to the
eye of an experienced Python programmer the exercises are written in quite an unidiomatic style - if you know the
language well, just know that we are not really using Python as Python, but instead as essentially executable
pseudocode, and are trying to prioritise people who haven't yet got the same level of expertise, and are thus likely to
have a harder time than you. If you're instead a beginner, be aware that as well as not using this or that feature of
the language, there are other ways in which the labs hide aspects of Python from you, and so if you would like to learn
it properly you will need to look further than this module, because again, this isn't about that. If you do want to
learn Python, though, you're in luck: even moreso than most other mainstream languages, there are _many_ resources
available online and in all sorts of formats - though remember that the best way to learn is by doing! In this lab, we
will at least cover the basics that you need to know to be able to complete the module, and at the end we will include
some disclaimers about particular differences from "normal" Python that are worth knowing if you want to go further with
learning the language.

The university computers have the main tools you need already installed, namely:
- [Python (version 3.11 or newer)](https://www.python.org/downloads/)
- [PyCharm (version 2023.1.1 or newer, Community Edition is fine)](https://www.jetbrains.com/pycharm/download/)
- [Git (almost any version should work)](https://git-scm.com/downloads)

Given that most of the time you spend working on these labs should be in your own time, rather than in the weekly
sessions, you may wish to install these on your own desktop/laptop. The links are above, and hopefully you should find
installation fairly painless, but if you do run into trouble, do try searching online, because they're very widely-used
tools, and you're likely not the only person to have had whatever the particular problem you're having is.

Even the lab computers, however, need a little extra setup.

First, open the Software Hub app on the lab machine. You can find it on your Desktop. Then launch "Git for Windows", "Python 3.11.3", and "PyCharm Community Edition".

Next, open a terminal and enter the command
```shell
git clone https://github.com/bertie-wheen/dsa-2023-4 dsa
```

This should create a `dsa/` directory, and you should enter
```shell
cd dsa
```
to move into it.

From this point onwards, all commands given are expected to be run from within this directory.
When you open a new terminal, though you don't need to `git clone` again, you should re-`cd`.

The first command to note is
```shell
git pull
```

If you run this now it won't have any effect, but the idea is to run it once a week, after the previous lab's solutions
and the next lab's exercises have been released, and it will then download that new material.

A command to be run now (and that needn't be run again) is
```shell
pip install textual
```

This will download and install a dependency of the testing framework.

Having done that, it's time to talk about PyCharm.

First, it's worth mentioning that you don't _have_ to use it. _However_, if the reason you don't want to use PyCharm is
because you live in Vim, note that there is a plugin
[(called IdeaVim)](https://www.jetbrains.com/help/pycharm/using-product-as-the-vim-editor.html) that enables
(customisable) Vim keybindings and is worth checking out. It won't turn PyCharm completely into Vim, but it might make
the experience sufficiently painless that you can enjoy the advantages the IDE offers.

If instead you don't want to use it because you're an avid Emacs user, there would be sense in the advice to not use it
just this once - but since you may be undiscourageable, it's worth noting that you can [configure PyCharm to use Emacs
as an external editor](https://www.jetbrains.com/help/pycharm/using-emacs-as-an-external-editor.html).

If you will only use VSCode, the recommended extension is
[`ms-python.python`](https://marketplace.visualstudio.com/items?itemName=ms-python.python), and there are some
preconfigured settings in `labs/.vscode/settings.json`, which will take effect if you "Open Folder" the `labs/`
directory. However, be warned that the extension - at least at the time of writing - does not render docstrings (or
rather the previews of them that appear e.g. on hover) properly. (They'll appear, but unparsed and unprettified.)

With all that said, PyCharm is recommended for this module, whatever you might otherwise use (unless you have
particularly strong feelings on the matter).

When opening it up, you should open the `labs/` subdirectory as a project.

You may then need to configure the Python interpreter. To do this, there's a little button on the right of the bottom
status bar, or you can go to `File -> Settings` (`Ctrl-Alt-S`), then `Project: labs -> Python Interpreter`. If it is not
already added, you should add the Python that's installed on your system.

Returning to the main IDE, you should look to the top-left, where it says `Project`. This is called a scope, and if you
click on it, then you'll see others, including two especially for this module. If you select `Exercises & Solutions`,
you'll notice that the directory/file tree simplifies, and then only contains the `exercise.py` and `solution.py` files.
This isn't necessary, but you may find that it makes it easier to see the files you actually care about, as there
are quite a few files that you shouldn't need to open or edit. The only other files that you're likely to be interested
in are the `README.md`s, and including those is what the `Exercises, Solutions & Notes` scope is for - however, the best
way to read these notes is [by using your web browser](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md).

With your environment set up, you should now continue on to
[this lab's core exercises](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/README.md).
