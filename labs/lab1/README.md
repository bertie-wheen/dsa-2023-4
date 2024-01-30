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

To use them, at the start of each session you should open the Software Hub app (which can be found on your Desktop), and
launch "Git for Windows", "Python 3.11.3", and "PyCharm Community Edition".

Given that most of the time you spend working on these labs should be in your own time, rather than in the weekly
sessions, you may wish to install these on your own computer. The links are above, and hopefully you should find
installation fairly painless, but if you do run into trouble, do try searching online, because they're very widely-used
tools, and you're likely not the only person to have had whatever the particular problem you're having is.

Having installed/activated the tools, open up PowerShell.

First, run
```shell
pip install textual
```
to install a dependency of the testing framework. If you're on your own computer you should only need to run this once,
but unfortunately if you're on a lab machine you'll need to re-run it at the start of each session, after activating
the tools from the Software Hub.

If you're on a lab machine, you should also run
```shell
cd N:/
```

This will change your directory to the shared drive, where files will persist between sessions and across machines. To
access this drive from home, [see this page in the UoS IT Guide](https://www.sussex.ac.uk/its/help/guide?id=49).

Now, from within `N:/` (or, if you prefer, a subdirectory of it), run the command
```shell
git clone https://github.com/bertie-wheen/dsa-2023-4 dsa
```

This should create a `dsa/` directory, and you should enter
```shell
cd dsa
```
to move into it.

From this point onwards, all commands given are expected to be run from within this `dsa/` directory.

Another command to know is
```shell
git pull
```

If you run this now it won't have any effect, but the idea is to run it once a week, after the previous lab's solutions
and the next lab's exercises have been released, at which point it will download that new material.

One note about it: If you're on a lab machine, running it will give an error, along the lines of
```
fatal: detected dubious ownership in repository at `//smbhome.uscs.susx.ac.uk/<username>/dsa`
`//smbhome.uscs.susx.ac.uk/<username>/dsa` is on a file system that doesnot record ownership
To add an exception for this directory, call:

        git config --global --add safe.directory '%(prefix)///smbhome.uscs.susx.ac.uk/<username>/dsa'
```

If you do what it recommends, and run
```shell
git config --global --add safe.directory '%(prefix)///smbhome.uscs.susx.ac.uk/<username>/dsa'
```
you'll then be able to successfully
```shell
git pull
```

(The bad news is that you'll need to do this once per session.)

Now it's time to talk about PyCharm.

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

When opening it up, you should open the `labs/` subdirectory (that is, `N:/dsa/labs/`) as a project.

You may then need to configure the Python interpreter. To do this, there's a little button on the right of the bottom
status bar, or you can go to `File -> Settings` (`Ctrl-Alt-S`), then `Project: labs -> Python Interpreter`. On the lab
machines it may have Python 3.9 configured by default, so you should set it to use 3.11 instead.
(`Add Interpreter -> Add Local Interpreter -> System Interpreter`.)

Returning to the main IDE, you should look to the top-left, where it says `Project`. This is called a scope, and if you
click on it, then you'll see others, including two especially for this module. If you select `Exercises & Solutions`,
you'll notice that the directory/file tree simplifies, and then only contains the `exercise.py` and `solution.py` files.
This isn't necessary, but you may find that it makes it easier to see the files you actually care about, as there
are quite a few files that you shouldn't need to open or edit. The only other files that you're likely to be interested
in are the `README.md`s, and including those is what the `Exercises, Solutions & Notes` scope is for - however, the best
way to read these notes is [by using your web browser](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md).

With your environment set up, you should now continue on to
[this lab's core exercises](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab1/core/README.md).
