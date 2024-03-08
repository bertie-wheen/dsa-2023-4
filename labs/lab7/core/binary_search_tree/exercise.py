"""
Data Structures & Algorithms

Lab 7: Binary Search Trees

Binary Search Trees Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.array import Array
from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Key, Value

from lab4.core.sorted_array_map import SortedArrayMap


class BinarySearchTree(Base[Key, Value]):
    """
    A binary search tree.

    Space: O(self.get_length())
    """

    _root: Optional["_BinarySearchSubtree[Key, Value]"]
    _length: int

    def __init__(self):
        """
        Initialize this binary search tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+
        """
        self._root = None
        self._length = 0

    @staticmethod
    def build(items: Iterator[tuple[Key, Value]]) -> "BinarySearchTree[Key, Value]":
        """
        Build a binary search tree containing the given items.

        +--------+-------------------------------------------------------------------------+
        | Time:  | O(build(items).get_length() * log2(build(items).get_length())) expected |
        +--------+-------------------------------------------------------------------------+
        | Space: | O(build(items).get_length())                                            |
        +--------+-------------------------------------------------------------------------+

        :parameter items: an iterator of initial items
        :returns: a minimal BST of those items
        """
        sorted_array_map = SortedArrayMap.build(items)
        array = Array.build(sorted_array_map.iterator())
        length = array.get_length()
        tree = BinarySearchTree()
        tree._root = BinarySearchTree._build(tree, array, 0, length - 1)
        tree._length = length
        return tree

    @staticmethod
    def _build(
        tree: "BinarySearchTree[Key, Value]",
        items: Array[tuple[Key, Value]],
        lower: int,
        upper: int,
    ) -> Optional["_BinarySearchSubtree[Key, Value]"]:
        if lower > upper:
            return None
        index = (lower + upper) // 2
        key, value = items.get_at(index)
        left = BinarySearchTree._build(tree, items, lower, index - 1)
        right = BinarySearchTree._build(tree, items, index + 1, upper)
        subtree = _BinarySearchSubtree(tree, key, value, left=left, right=right)
        if left is not None:
            left._parent = subtree
        if right is not None:
            right._parent = subtree
        return subtree

    def contains(self, key: Key) -> bool:
        """
        Check if this BST contains the given key.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: ``True`` if the key is in the BST, else ``False``
        """
        if self.is_empty():
            return False
        return self._root.contains(key)

    def is_empty(self) -> bool:
        """
        Check if this BST is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the BST is empty, else ``False``
        """
        return self._root is None

    def get_length(self) -> int:
        """
        Get the number of items in this BST.

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
        Get the number of levels below the root of this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the height
        """
        if self.is_empty():
            return -1
        return self._root.get_height()

    def _get_subtree(self, key: Key) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the subtree with the given key within this BST.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key that the subtree should have
        :returns: the subtree with that key
        :raises KeyError: if there is no subtree with the key
        """
        if self.is_empty():
            raise KeyError
        return self._root.get_subtree(key)

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this BST.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key is not in the BST
        """
        subtree = self._get_subtree(key)
        return subtree.get_value()

    def get_minimum_key(self) -> Key:
        """
        Get the minimum key in this BST.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the minimum key
        :raises EmptyCollectionError: if the BST is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        minimum = self._root.get_minimum()
        return minimum.get_key()

    def get_maximum_key(self) -> Key:
        """
        Get the maximum key in this BST.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the maximum key
        :raises EmptyCollectionError: if the BST is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        maximum = self._root.get_maximum()
        return maximum.get_key()

    def get_previous_key(self, key: Key) -> Key:
        """
        Get the given key's (in-order) predecessor.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the previous key
        """
        subtree = self._get_subtree(key)
        previous = subtree.get_previous()
        return previous.get_key()

    def get_next_key(self, key: Key) -> Key:
        """
        Get the given key's (in-order) successor.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the next key
        """
        subtree = self._get_subtree(key)
        next = subtree.get_next()
        return next.get_key()

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this BST.
        If the key is already in the BST, set it to map to the new value.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        if self.is_empty():
            self._root = _BinarySearchSubtree(self, key, new_value)
            self._length = 1
        else:
            self._root.insert(key, new_value)

    def remove(self, key: Key) -> Value:
        """
        Remove the mapping for the given key from this BST, and return the value that it mapped to.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if the key was not in the BST
        """
        subtree = self._get_subtree(key)
        value = subtree.get_value()
        subtree.remove()
        return value

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        """
        Get an iterator over the key/value pairs in this BST.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the BST's items, sorted by key
        """
        if not self.is_empty():
            yield from self._root.iterator()

    def keys_iterator(self) -> Iterator[Key]:
        """
        Get an iterator over the keys in this BST.
        The iteration order is unspecified.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the BST's keys, in sorted order
        """
        for key, value in self.iterator():
            yield key

    def values_iterator(self) -> Iterator[Value]:
        """
        Get an iterator over the values in this BST.
        The iteration order is unspecified.
        If the same value is mapped to by multiple keys, it will occur multiple times.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the BST's values
        """
        for key, value in self.iterator():
            yield value


class _BinarySearchSubtree(Base[Key, Value]):
    """
    A subtree in a binary search tree.

    Space: O(self.get_length())
    """

    _tree: BinarySearchTree[Key, Value]
    _key: Key
    _value: Value
    _parent: Optional["_BinarySearchSubtree[Key, Value]"]
    _left: Optional["_BinarySearchSubtree[Key, Value]"]
    _right: Optional["_BinarySearchSubtree[Key, Value]"]

    def __init__(
        self,
        tree: BinarySearchTree[Key, Value],
        key: Key,
        value: Value,
        parent: Optional["_BinarySearchSubtree[Key, Value]"] = None,
        left: Optional["_BinarySearchSubtree[Key, Value]"] = None,
        right: Optional["_BinarySearchSubtree[Key, Value]"] = None,
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
        :parameter left: the left subtree, if there is one (default ``None``)
        :parameter right: the right subtree, if there is one (default ``None``)
        """
        self._tree = tree
        self._key = key
        self._value = value
        self._parent = parent
        self._left = left
        self._right = right

    def ascend_left(self) -> "_BinarySearchSubtree[Key, Value]":
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

    def ascend_right(self) -> "_BinarySearchSubtree[Key, Value]":
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

    def descend_left(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the subtree reached by descending leftwards as far as possible.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the reached descendent
        """
        if self.is_left_empty():
            return self
        return self._left.descend_left()

    def descend_right(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the subtree reached by descending rightwards as far as possible.

        # +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the reached descendent
        """
        if self.is_right_empty():
            return self
        return self._right.descend_right()

    def contains(self, key: Key) -> bool:
        """
        Check if this subtree contains the given key.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

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

    def get_height(self) -> int:
        """
        Get the number of levels below the root of this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the height
        """
        max_child_height = -1
        if self.has_left():
            max_child_height = self._left.get_height()
        if self.has_right():
            max_child_height = max(max_child_height, self._right.get_height())
        return 1 + max_child_height

    def get_subtree(self, key: Key) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the subtree with the given key within this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key that the subtree should have
        :returns: the subtree with the given key
        :raises KeyError: if there is no descendent subtree with the key
        """
        raise NotImplementedError

    def get(self, key: Key) -> Value:
        """
        Get the value mapped to by the given key in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :returns: the corresponding value
        :raises KeyError: if there is no descendent subtree with the key
        """
        subtree = self.get_subtree(key)
        return subtree._value

    def get_minimum(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the minimum subtree amongst the subtree's descendents.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the minimum subtree
        """
        raise NotImplementedError

    def get_maximum(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get the maximum subtree amongst the subtree's descendents.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the maximum subtree
        """
        raise NotImplementedError

    def get_previous(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get this subtree's (in-order) predecessor.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the previous subtree
        """
        raise NotImplementedError

    def get_next(self) -> "_BinarySearchSubtree[Key, Value]":
        """
        Get this subtree's (in-order) successor.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: the next subtree
        """
        raise NotImplementedError

    def insert(self, key: Key, new_value: Value) -> None:
        """
        Insert the given key/value mapping into this subtree.
        If the key is already in the subtree, set it to map to the new value.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter key: the key
        :parameter new_value: the new value that that key should map to
        """
        raise NotImplementedError

    def remove(self) -> None:
        """
        Remove this subtree's key/value mapping from the tree.

        +--------+----------------------+
        | Time:  | O(self.get_height()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+
        """
        raise NotImplementedError

    def iterator(self) -> Iterator[tuple[Key, Value]]:
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
        yield self._key, self._value
        if self.has_right():
            yield from self._right.iterator()
