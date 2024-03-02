from lib.iterator import iterator
from lib.test import Test

from lab6.core.binary_tree.exercise import BinaryTree, BinarySubtree


@Test
def create_example_bottom_up_doesnt_error():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 0
    yield 0


@Test
def create_example_top_down_doesnt_error():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 0
    yield 0


@Test
def create_example_in_bits_then_link_doesnt_error():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 0
    yield 0


@Test
def contains_a_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("a")


@Test
def contains_b_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("b")


@Test
def contains_c_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("c")


@Test
def contains_d_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("d")


@Test
def contains_e_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("e")


@Test
def contains_f_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("f")


@Test
def contains_g_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield tree.contains("g")


@Test
def contains_a_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield a.contains("a")


@Test
def contains_b_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield a.contains("b")


@Test
def contains_c_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield a.contains("c")


@Test
def contains_d_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield a.contains("d")


@Test
def contains_e_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield a.contains("e")


@Test
def contains_f_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield a.contains("f")


@Test
def contains_g_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield a.contains("g")


@Test
def contains_a_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("a")


@Test
def contains_b_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield b.contains("b")


@Test
def contains_c_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("c")


@Test
def contains_d_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("d")


@Test
def contains_e_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("e")


@Test
def contains_f_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("f")


@Test
def contains_g_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield b.contains("g")


@Test
def contains_a_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("a")


@Test
def contains_b_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("b")


@Test
def contains_c_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("c")


@Test
def contains_d_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("d")


@Test
def contains_e_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("e")


@Test
def contains_f_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("f")


@Test
def contains_g_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield c.contains("g")


@Test
def contains_a_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("a")


@Test
def contains_b_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("b")


@Test
def contains_c_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("c")


@Test
def contains_d_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield d.contains("d")


@Test
def contains_e_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("e")


@Test
def contains_f_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("f")


@Test
def contains_g_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield d.contains("g")


@Test
def contains_a_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield e.contains("a")


@Test
def contains_b_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield e.contains("b")


@Test
def contains_c_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield e.contains("c")


@Test
def contains_d_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield e.contains("d")


@Test
def contains_e_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield e.contains("e")


@Test
def contains_f_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield e.contains("f")


@Test
def contains_g_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield e.contains("g")


@Test
def contains_a_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("a")


@Test
def contains_b_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("b")


@Test
def contains_c_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("c")


@Test
def contains_d_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("d")


@Test
def contains_e_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("e")


@Test
def contains_f_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield f.contains("f")


@Test
def contains_g_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield f.contains("g")


@Test
def contains_a_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield g.contains("a")


@Test
def contains_b_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield g.contains("b")


@Test
def contains_c_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield False
    yield g.contains("c")


@Test
def contains_d_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield g.contains("d")


@Test
def contains_e_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield g.contains("e")


@Test
def contains_f_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield g.contains("f")


@Test
def contains_g_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield True
    yield g.contains("g")


@Test
def get_level_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield a.get_level()


@Test
def get_level_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 2
    yield b.get_level()


@Test
def get_level_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 0
    yield c.get_level()


@Test
def get_level_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 3
    yield d.get_level()


@Test
def get_level_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 2
    yield e.get_level()


@Test
def get_level_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 3
    yield f.get_level()


@Test
def get_level_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield g.get_level()


@Test
def get_level_on_top_down_example_a():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield a.get_level()


@Test
def get_level_on_top_down_example_b():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 2
    yield b.get_level()


@Test
def get_level_on_top_down_example_c():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 0
    yield c.get_level()


@Test
def get_level_on_top_down_example_d():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 3
    yield d.get_level()


@Test
def get_level_on_top_down_example_e():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 2
    yield e.get_level()


@Test
def get_level_on_top_down_example_f():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 3
    yield f.get_level()


@Test
def get_level_on_top_down_example_g():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield g.get_level()


@Test
def get_level_on_bits_then_link_example_a():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield a.get_level()


@Test
def get_level_on_bits_then_link_example_b():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 2
    yield b.get_level()


@Test
def get_level_on_bits_then_link_example_c():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 0
    yield c.get_level()


@Test
def get_level_on_bits_then_link_example_d():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 3
    yield d.get_level()


@Test
def get_level_on_bits_then_link_example_e():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 2
    yield e.get_level()


@Test
def get_level_on_bits_then_link_example_f():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 3
    yield f.get_level()


@Test
def get_level_on_bits_then_link_example_g():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield g.get_level()


@Test
def get_length_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 7
    yield tree.get_length()


@Test
def get_length_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 2
    yield a.get_length()


@Test
def get_length_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield b.get_length()


@Test
def get_length_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 7
    yield c.get_length()


@Test
def get_length_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield d.get_length()


@Test
def get_length_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 3
    yield e.get_length()


@Test
def get_length_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield f.get_length()


@Test
def get_length_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 4
    yield g.get_length()


@Test
def get_length_on_top_down_example():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 7
    yield tree.get_length()


@Test
def get_length_on_top_down_example_a():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 2
    yield a.get_length()


@Test
def get_length_on_top_down_example_b():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield b.get_length()


@Test
def get_length_on_top_down_example_c():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 7
    yield c.get_length()


@Test
def get_length_on_top_down_example_d():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield d.get_length()


@Test
def get_length_on_top_down_example_e():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 3
    yield e.get_length()


@Test
def get_length_on_top_down_example_f():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield f.get_length()


@Test
def get_length_on_top_down_example_g():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 4
    yield g.get_length()


@Test
def get_length_on_bits_then_link_example():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 7
    yield tree.get_length()


@Test
def get_length_on_bits_then_link_example_a():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 2
    yield a.get_length()


@Test
def get_length_on_bits_then_link_example_b():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield b.get_length()


@Test
def get_length_on_bits_then_link_example_c():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 7
    yield c.get_length()


@Test
def get_length_on_bits_then_link_example_d():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield d.get_length()


@Test
def get_length_on_bits_then_link_example_e():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 3
    yield e.get_length()


@Test
def get_length_on_bits_then_link_example_f():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield f.get_length()


@Test
def get_length_on_bits_then_link_example_g():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 4
    yield g.get_length()


@Test
def get_height_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 3
    yield tree.get_height()


@Test
def get_height_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield a.get_height()


@Test
def get_height_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 0
    yield b.get_height()


@Test
def get_height_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 3
    yield c.get_height()


@Test
def get_height_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 0
    yield d.get_height()


@Test
def get_height_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 1
    yield e.get_height()


@Test
def get_height_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 0
    yield f.get_height()


@Test
def get_height_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield 2
    yield g.get_height()


@Test
def get_height_on_top_down_example():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 3
    yield tree.get_height()


@Test
def get_height_on_top_down_example_a():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield a.get_height()


@Test
def get_height_on_top_down_example_b():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 0
    yield b.get_height()


@Test
def get_height_on_top_down_example_c():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 3
    yield c.get_height()


@Test
def get_height_on_top_down_example_d():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 0
    yield d.get_height()


@Test
def get_height_on_top_down_example_e():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 1
    yield e.get_height()


@Test
def get_height_on_top_down_example_f():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 0
    yield f.get_height()


@Test
def get_height_on_top_down_example_g():
    tree = BinaryTree()
    c = BinarySubtree(item="c")
    tree.insert_root(c)
    a = BinarySubtree(item="a")
    c.insert_left(a)
    g = BinarySubtree(item="g")
    c.insert_right(g)
    b = BinarySubtree(item="b")
    a.insert_right(b)
    e = BinarySubtree(item="e")
    g.insert_left(e)
    d = BinarySubtree(item="d")
    e.insert_left(d)
    f = BinarySubtree(item="f")
    e.insert_right(f)
    yield 2
    yield g.get_height()


@Test
def get_height_on_bits_then_link_example():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 3
    yield tree.get_height()


@Test
def get_height_on_bits_then_link_example_a():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield a.get_height()


@Test
def get_height_on_bits_then_link_example_b():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 0
    yield b.get_height()


@Test
def get_height_on_bits_then_link_example_c():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 3
    yield c.get_height()


@Test
def get_height_on_bits_then_link_example_d():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 0
    yield d.get_height()


@Test
def get_height_on_bits_then_link_example_e():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 1
    yield e.get_height()


@Test
def get_height_on_bits_then_link_example_f():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 0
    yield f.get_height()


@Test
def get_height_on_bits_then_link_example_g():
    tree = BinaryTree()
    a = BinarySubtree(item="a")
    b = BinarySubtree(item="b")
    c = BinarySubtree(item="c")
    d = BinarySubtree(item="d")
    e = BinarySubtree(item="e")
    f = BinarySubtree(item="f")
    g = BinarySubtree(item="g")
    a.insert_right(b)
    c.insert_left(a)
    e.insert_left(d)
    e.insert_right(f)
    g.insert_left(e)
    c.insert_right(g)
    tree.insert_root(c)
    yield 2
    yield g.get_height()


@Test
def pre_iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("c", "a", "b", "g", "e", "d", "f")
    yield tree.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("a", "b")
    yield a.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("c", "a", "b", "g", "e", "d", "f")
    yield c.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("e", "d", "f")
    yield e.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.pre_iterator()


@Test
def pre_iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("g", "e", "d", "f")
    yield g.pre_iterator()


@Test
def iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("a", "b", "c", "d", "e", "f", "g")
    yield tree.iterator()


@Test
def iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("a", "b")
    yield a.iterator()


@Test
def iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.iterator()


@Test
def iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("a", "b", "c", "d", "e", "f", "g")
    yield c.iterator()


@Test
def iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.iterator()


@Test
def iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d", "e", "f")
    yield e.iterator()


@Test
def iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.iterator()


@Test
def iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d", "e", "f", "g")
    yield g.iterator()


@Test
def post_iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b", "a", "d", "f", "e", "g", "c")
    yield tree.post_iterator()


@Test
def post_iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b", "a")
    yield a.post_iterator()


@Test
def post_iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.post_iterator()


@Test
def post_iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b", "a", "d", "f", "e", "g", "c")
    yield c.post_iterator()


@Test
def post_iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.post_iterator()


@Test
def post_iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d", "f", "e")
    yield e.post_iterator()


@Test
def post_iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.post_iterator()


@Test
def post_iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d", "f", "e", "g")
    yield g.post_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("c", "g", "e", "f", "d", "a", "b")
    yield tree.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("a", "b")
    yield a.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("c", "g", "e", "f", "d", "a", "b")
    yield c.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("e", "f", "d")
    yield e.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.reverse_pre_iterator()


@Test
def reverse_pre_iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("g", "e", "f", "d")
    yield g.reverse_pre_iterator()


@Test
def reverse_iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("g", "f", "e", "d", "c", "b", "a")
    yield tree.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b", "a")
    yield a.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("g", "f", "e", "d", "c", "b", "a")
    yield c.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f", "e", "d")
    yield e.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.reverse_iterator()


@Test
def reverse_iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("g", "f", "e", "d")
    yield g.reverse_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f", "d", "e", "g", "b", "a", "c")
    yield tree.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_a():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b", "a")
    yield a.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_b():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("b")
    yield b.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_c():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f", "d", "e", "g", "b", "a", "c")
    yield c.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_d():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("d")
    yield d.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_e():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f", "d", "e")
    yield e.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_f():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f")
    yield f.reverse_post_iterator()


@Test
def reverse_post_iterator_on_bottom_up_example_g():
    d = BinarySubtree(item="d")
    f = BinarySubtree(item="f")
    b = BinarySubtree(item="b")
    e = BinarySubtree(item="e", left=d, right=f)
    a = BinarySubtree(item="a", right=b)
    g = BinarySubtree(item="g", left=e)
    c = BinarySubtree(item="c", left=a, right=g)
    tree = BinaryTree(root=c)
    yield iterator("f", "d", "e", "g")
    yield g.reverse_post_iterator()
