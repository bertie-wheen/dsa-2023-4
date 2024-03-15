"""
Data Structures & Algorithms

Lab 8: AVL Trees

AVL Trees Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.array import Array
from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Key, Value

from lab4.core.sorted_array_map import SortedArrayMap


class AVLTree(Base[Key, Value]):
    """
    An AVL tree.

    Space: O(self.get_length())
    """

    _length: int
    _root: Optional["_AVLSubtree[Key, Value]"]

    def __init__(self) -> None:
        """
        Initialize this AVL tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._length = 0
        self._root = None

    @staticmethod
    def build(items: Iterator[tuple[Key, Value]]) -> "AVLTree[Key, Value]":
        """
        Build an AVL tree containing the given items.

        +--------+----------------------------------------------------------------+
        | Time:  | O(build(items).get_length() * log2(build(items).get_length())) |
        +--------+----------------------------------------------------------------+
        | Space: | O(build(items).get_length())                                   |
        +--------+----------------------------------------------------------------+

        :parameter items: an iterator of initial items
        :returns: an AVL tree of those items
        """
        sorted_array_map = SortedArrayMap.build(items)
        array = Array.build(sorted_array_map.iterator())
        length = array.get_length()
        tree = AVLTree()
        tree._root = AVLTree._build(tree, array, 0, length - 1)
        tree._length = length
        return tree

    @staticmethod
    def _build(
        tree: "AVLTree[Key, Value]",
        items: Array[tuple[Key, Value]],
        lower: int,
        upper: int,
    ) -> Optional["_AVLSubtree[Key, Value]"]:
        if lower > upper:
            return None
        index = (lower + upper) // 2
        key, value = items.get_at(index)
        left = AVLTree._build(tree, items, lower, index - 1)
        right = AVLTree._build(tree, items, index + 1, upper)
        subtree = _AVLSubtree(tree, key, value)
        if left is not None:
            subtree._left = left
            left._parent = subtree
        if right is not None:
            subtree._right = right
            right._parent = subtree
        subtree.recalculate()
        return subtree

    def contains(self, key: Key) -> bool:
        """
        Check if this AVL tree contains the given key.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: ``True`` if the key is in the tree, else ``False``
        """
        if self.is_empty():
            return False
        return self._root.contains(key)

    def is_empty(self) -> bool:
        """
        Check if this AVL tree is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the tree is empty, else ``False``
        """
        return self._root is None

    def get_length(self) -> int:
        """
        Get the number of items in this AVL tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._length

    def get_height(self) -> int:
        """
        Get the number of levels below the root of this AVL tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the height
        """
        if self.is_empty():
            return -1
        return self._root.get_height()

    def _get_subtree(self, key: Key) -> '_AVLSubtree[Key, Value]':
        """
        Get the subtree with the given key within this AVL tree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key that the subtree should have
        :returns: the subtree with that key
        :raises KeyError: if there is no subtree with the key
        """
        if self.is_empty():
            raise KeyError
        return self._root.get_subtree(key)

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this AVL tree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key is not in the tree
        """
        subtree = self._get_subtree(key)
        return subtree.get_value()

    def get_minimum_key(self) -> Key:
        """
        Get the minimum key in this AVL tree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the minimum key
        :raises EmptyCollectionError: if the tree is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        minimum = self._root.get_minimum()
        return minimum.get_key()

    def get_maximum_key(self) -> Key:
        """
        Get the maximum key in this AVL tree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the maximum key
        :raises EmptyCollectionError: if the tree is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        maximum = self._root.get_maximum()
        return maximum.get_key()

    def get_previous_key(self, key: Key) -> Key:
        """
        Get the given key's (in-order) predecessor.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the previous key
        """
        subtree = self._get_subtree(key)
        previous = subtree.get_previous()
        return previous.get_key()

    def get_next_key(self, key: Key) -> Key:
        """
        Get the given key's (in-order) successor.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the next key
        """
        subtree = self._get_subtree(key)
        next = subtree.get_next()
        return next.get_key()

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this AVL tree.
        If the key is already in the tree, set it to map to the new value.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        if self.is_empty():
            self._root = _AVLSubtree(self, key, new_value)
            self._length = 1
        else:
            self._root.insert(key, new_value)

    def remove(self, key: Key) -> Value:
        """
        Remove the mapping for the given key from this AVL tree, and return the value that it mapped to.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key was not in the tree
        """
        subtree = self._get_subtree(key)
        value = subtree.get_value()
        subtree.remove()
        return value

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        """
        Get an iterator over the key/value pairs in this AVL tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, sorted by key
        """
        if self.is_empty():
            return
        for subtree in self._root.iterator():
            yield subtree.get_key(), subtree.get_value()

    def keys_iterator(self) -> Iterator[Key]:
        """
        Get an iterator over the keys in this AVL tree.
        The iteration order is unspecified.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's keys, in sorted order
        """
        for key, value in self.iterator():
            yield key

    def values_iterator(self) -> Iterator[Value]:
        """
        Get an iterator over the values in this AVL tree.
        The iteration order is unspecified.
        If the same value is mapped to by multiple keys, it will occur multiple times.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's values
        """
        for key, value in self.iterator():
            yield value


# noinspection PyProtectedMember
class _AVLSubtree(Base[Key, Value]):
    """
    A subtree in a binary search tree.

    Space: O(self.get_length())
    """

    _balance_factor: int
    _height: int
    _tree: AVLTree[Key, Value]
    _key: Key
    _value: Value
    _parent: Optional["_AVLSubtree[Key, Value]"]
    _left: Optional["_AVLSubtree[Key, Value]"]
    _right: Optional["_AVLSubtree[Key, Value]"]

    def __init__(
        self,
        tree: AVLTree[Key, Value],
        key: Key,
        value: Value,
        parent: Optional["_AVLSubtree[Key, Value]"] = None,
    ) -> None:
        """
        Initialize this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter tree: the containing tree
        :parameter key: the key this subtree contains at its root
        :parameter value: the value this subtree contains at its root
        :parameter parent: the parent subtree, if there is one (default ``None``)
        """
        self._balance_factor = 0
        self._height = 0
        self._tree = tree
        self._key = key
        self._value = value
        self._parent = parent
        self._left = None
        self._right = None

    def ascend_left(self) -> "_AVLSubtree[Key, Value]":
        """
        Get the subtree reached by ascending leftwards as far as possible.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the reached ancestor
        """
        if self.is_right():
            return self._parent.ascend_left()
        return self

    def ascend_right(self) -> "_AVLSubtree[Key, Value]":
        """
        Get the subtree reached by ascending rightwards as far as possible.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the reached ancestor
        """
        if self.is_left():
            return self._parent.ascend_right()
        return self

    def descend_left(self) -> "_AVLSubtree[Key, Value]":
        """
        Get the subtree reached by descending leftwards as far as possible.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the reached descendent
        """
        if self.is_left_empty():
            return self
        return self._left.descend_left()

    def descend_right(self) -> "_AVLSubtree[Key, Value]":
        """
        Get the subtree reached by descending rightwards as far as possible.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the reached descendent
        """
        if self.is_right_empty():
            return self
        return self._right.descend_right()

    def contains(self, key: Key) -> bool:
        """
        Check if this subtree contains the given key.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key to search for
        :returns: ``True`` if the key is in the subtree, else ``False``
        """
        if key < self._key:
            return self.has_left() and self._left.contains(key)
        if key > self._key:
            return self.has_right() and self._right.contains(key)
        return True

    def has_parent(self) -> bool:
        """
        Check if this subtree has a parent subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there's a parent, else ``False``
        """
        return self._parent is not None

    def has_left(self) -> bool:
        """
        Check if this subtree has a left child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there's a left subtree, else ``False``
        """
        return self._left is not None

    def has_right(self) -> bool:
        """
        Check if this subtree has a right child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there's a right subtree, else ``False``
        """
        return self._right is not None

    def is_root(self) -> bool:
        """
        Check if this is the root subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if it's the root subtree, else ``False``
        """
        return self._tree._root is self

    def is_leaf(self) -> bool:
        """
        Check if this subtree has no children.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there're no children, else ``False``
        """
        return self.is_left_empty() and self.is_right_empty()

    def is_left_empty(self) -> bool:
        """
        Check if the left subtree is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the left subtree is empty, else ``False``
        """
        return self._left is None

    def is_right_empty(self) -> bool:
        """
        Check if the right subtree is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the right subtree is empty, else ``False``
        """
        return self._right is None

    def is_left(self) -> bool:
        """
        Check if this subtree has a parent, and that it's its left child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the subtree is a left child, else ``False``
        """
        return self.has_parent() and self._parent._left is self

    def is_right(self) -> bool:
        """
        Check if this subtree has a parent, and that it's its right child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the subtree is a right child, else ``False``
        """
        return self.has_parent() and self._parent._right is self

    def get_key(self) -> Key:
        """
        Get the key at the root of this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the key
        """
        return self._key

    def get_value(self) -> Value:
        """
        Get the value at the root of this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the value
        """
        return self._value

    def get_balance_factor(self) -> int:
        """
        Get the balance factor of this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the balance factor
        """
        return self._balance_factor

    def get_height(self) -> int:
        """
        Get the number of levels below the root of this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the height
        """
        return self._height

    def get_left_height(self) -> int:
        """
        Get the number of levels below the root of the left subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the left subtree height
        """
        if self.is_left_empty():
            return -1
        return self._left._height

    def get_right_height(self) -> int:
        """
        Get the number of levels below the root of the right subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the right subtree height
        """
        if self.is_right_empty():
            return -1
        return self._right._height

    def get_subtree(self, key: Key) -> '_AVLSubtree[Key, Value]':
        """
        Get the subtree with the given key within this subtree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key that the subtree should have
        :returns: the subtree with the given key
        :raises KeyError: if there is no descendent subtree with the key
        """
        if key < self._key:
            if self.is_left_empty():
                raise KeyError
            return self._left.get_subtree(key)
        if key > self._key:
            if self.is_right_empty():
                raise KeyError
            return self._right.get_subtree(key)
        return self

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this subtree.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if there is no descendent subtree with the key
        """
        subtree = self.get_subtree(key)
        return subtree._value

    def get_minimum(self) -> '_AVLSubtree[Key, Value]':
        """
        Get the minimum subtree amongst the subtree's descendents.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the minimum subtree
        """
        return self.descend_left()

    def get_maximum(self) -> '_AVLSubtree[Key, Value]':
        """
        Get the maximum subtree amongst the subtree's descendents.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the maximum subtree
        """
        return self.descend_right()

    def get_previous(self) -> '_AVLSubtree[Key, Value]':
        """
        Get this subtree's (in-order) predecessor.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the previous subtree
        """
        if self.has_left():
            return self._left.descend_right()
        ancestor = self.ascend_right()
        if ancestor.is_root():
            raise KeyError
        return ancestor._parent

    def get_next(self) -> '_AVLSubtree[Key, Value]':
        """
        Get this subtree's (in-order) successor.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: the next subtree
        """
        if self.has_right():
            return self._right.descend_left()
        ancestor = self.ascend_left()
        if ancestor.is_root():
            raise KeyError
        return ancestor._parent

    def rotate_cw(self) -> None:
        """
        Rotate clockwise, making this subtree's left child its parent.

        Recalculate balance factors and heights, but not for any ancestors further up in the tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :raises ValueError: if there is no left child
        """
        raise NotImplementedError

    def rotate_acw(self) -> None:
        """
        Rotate anticlockwise, making this subtree's right child its parent.

        Recalculate balance factors and heights, but not for any ancestors further up in the tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :raises ValueError: if there is no right child
        """
        raise NotImplementedError

    def recalculate(self) -> None:
        """
        Recalculate this subtree's balance factor and height.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        raise NotImplementedError

    def rebalance(self) -> bool:
        """
        If this subtree has become unbalanced, i.e. its balance factor is now -2 or +2, rebalance it using one or two
        rotations, and return ``True`` - otherwise, if its balance factor is still between -1 and +1, do nothing and
        return ``False``.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if rebalancing was required, else ``False``
        """
        raise NotImplementedError

    def update_ancestors(self, can_stop_after_rebalance: bool) -> None:
        """
        Update this subtree's ancestors (starting with itself) after an insertion or removal.

        Recalculate balance factors and heights, and rotate as needed to rebalance any now-unbalanced ancestors.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :parameter can_stop_after_rebalance: whether traversal up the ancestor chain can stop after a rebalance
        """
        self.recalculate()
        rebalanced = self.rebalance()
        if rebalanced and can_stop_after_rebalance:
            return
        if self.has_parent():
            self._parent.update_ancestors(can_stop_after_rebalance)

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this subtree.
        If the key is already in the subtree, set it to map to the new value.

        +--------+----------------------------------+
        | Time:  | O(log2(self._tree.get_length())) |
        +--------+----------------------------------+
        | Space: | O(1)                             |
        +--------+----------------------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        if key == self._key:
            self._value = new_value
            return
        if key < self._key:
            if self.has_left():
                self._left.insert(key, new_value)
                return
            self._left = _AVLSubtree(self._tree, key, new_value, parent=self)
        else:
            if self.has_right():
                self._right.insert(key, new_value)
                return
            self._right = _AVLSubtree(self._tree, key, new_value, parent=self)
        self._tree._length += 1
        self.update_ancestors(True)

    def remove(self):
        """
        Remove this subtree's key/value mapping from the tree.

        +--------+----------------------------------+
        | Time:  | O(log2(self._tree.get_length())) |
        +--------+----------------------------------+
        | Space: | O(1)                             |
        +--------+----------------------------------+
        """
        if self.is_leaf():
            self._tree._length -= 1
            if self.is_root():
                self._tree._root = None
            else:
                if self.is_left():
                    self._parent._left = None
                else:
                    self._parent._right = None
                self._parent.update_ancestors(False)
            return
        if self.has_left():
            subtree = self.get_previous()
        else:
            subtree = self.get_next()
        self._key = subtree._key
        self._value = subtree._value
        subtree.remove()

    def iterator(self) -> Iterator['_AVLSubtree[Key, Value]']:
        """
        Get an iterator over the key/value pairs in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, sorted by key
        """
        if self.has_left():
            yield from self._left.iterator()
        yield self
        if self.has_right():
            yield from self._right.iterator()
