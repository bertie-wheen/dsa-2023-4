"""
Data Structures & Algorithms

Lab 6: Binary Trees & Traversals

Binary Trees Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.array import Array
from lib.base import Base
from lib.type_vars import Item


class BinaryTree(Base[Item]):
    """
    A binary tree.

    Space: O(self.get_length())
    """

    _root: Optional["BinarySubtree[Item]"]

    def __init__(self, root: Optional["BinarySubtree[Item]"] = None) -> None:
        """
        Initialize this binary tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter root: the root subtree (default None)
        :raises ValueError: if ``root`` is given and has a parent
        """
        self._root = None
        if root is not None:
            self.insert_root(root)

    @staticmethod
    def build(items: Iterator[Item]) -> "BinaryTree[Item]":
        """
        Build a binary tree containing the given items.

        The tree's in-order iterator will behave like the one given, in that it yields the items in the same order.

        +--------+------------------------------+
        | Time:  | O(build(items).get_length()) |
        +--------+------------------------------+
        | Space: | O(build(items).get_length()) |
        +--------+------------------------------+

        :parameter items: an iterator of initial items
        :returns: a binary tree of those items
        """
        array = Array.build(items)
        root = BinaryTree._build(array, 0, array.get_length() - 1)
        return BinaryTree(root=root)

    @staticmethod
    def _build(items: Array[Item], lower: int, upper: int) -> Optional["BinarySubtree[Item]"]:
        if lower > upper:
            return None
        index = (lower + upper) // 2
        item = items.get_at(index)
        left = BinaryTree._build(items, lower, index - 1)
        right = BinaryTree._build(items, index + 1, upper)
        return BinarySubtree(item, left=left, right=right)

    def contains(self, item: Item) -> bool:
        """
        Check if this tree contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter item: the item to check membership of
        :returns: ``True`` if the item is in the tree, else ``False``
        """
        if self.is_empty():
            return False
        return self._root.contains(item)

    def is_empty(self) -> bool:
        """
        Check if this tree is empty.

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
        Get the number of items in this tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        if self.is_empty():
            return 0
        return self._root.get_length()

    def get_height(self) -> int:
        """
        Get the number of levels below the root of this tree.

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

    def get_root(self) -> Optional["BinarySubtree[Item]"]:
        """
        Get the root subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the root subtree
        """
        return self._root

    def insert_root(self, new_root: "BinarySubtree[Item]") -> None:
        """
        Insert the given subtree as the root of this tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_root: the new root subtree
        :raises ValueError: if there's already a root or ``new_root`` has a parent
        """
        if not self.is_empty():
            raise ValueError
        if not new_root.is_root():
            raise ValueError
        self._root = new_root

    def remove_root(self) -> "BinarySubtree[Item]":
        """
        Remove and return the root subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the old root subtree
        :raises ValueError: if there is no root
        """
        if self.is_empty():
            raise ValueError
        old_root = self._root
        self._root = None
        return old_root

    def pre_iterator(self) -> Iterator[Item]:
        """
        Get a pre-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, root-left-right
        """
        if not self.is_empty():
            yield from self._root.pre_iterator()

    def iterator(self) -> Iterator[Item]:
        """
        Get an in-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, left-root-right
        """
        if not self.is_empty():
            yield from self._root.iterator()

    def post_iterator(self) -> Iterator[Item]:
        """
        Get a post-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, left-right-root
        """
        if not self.is_empty():
            yield from self._root.post_iterator()

    def reverse_pre_iterator(self) -> Iterator[Item]:
        """
        Get a reverse pre-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, root-right-left
        """
        if not self.is_empty():
            yield from self._root.reverse_pre_iterator()

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse in-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, right-root-left
        """
        if not self.is_empty():
            yield from self._root.reverse_iterator()

    def reverse_post_iterator(self) -> Iterator[Item]:
        """
        Get a reverse post-order iterator over the items in this tree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the tree's items, right-left-root
        """
        if not self.is_empty():
            yield from self._root.reverse_post_iterator()


class BinarySubtree(Base[Item]):
    """
    A binary subtree.

    Space: O(self.get_length())
    """

    _item: Item
    _parent: Optional["BinarySubtree[Item]"]
    _left: Optional["BinarySubtree[Item]"]
    _right: Optional["BinarySubtree[Item]"]
    _length: int
    _height: int

    def __init__(
        self,
        item: Item,
        left: Optional["BinarySubtree[Item]"] = None,
        right: Optional["BinarySubtree[Item]"] = None,
    ) -> None:
        """
        Initialize this binary tree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter item: the root item
        :parameter left: the left subtree (default None)
        :parameter right: the right subtree (default None)
        :raises ValueError: if either of the left or right subtrees are given and have a parent
        """
        if left is not None and not left.is_root():
            raise ValueError
        if right is not None and not right.is_root():
            raise ValueError
        if left is not None:
            left._parent = self
        if right is not None:
            right._parent = self
        self._item = item
        self._parent = None
        self._left = left
        self._right = right
        self._length = self._calculate_length()
        self._height = self._calculate_height()

    def left_contains(self, item: Item) -> bool:
        """
        Check if the left subtree contains the given item.

        +--------+---------------------------+
        | Time:  | O(self.get_left_length()) |
        +--------+---------------------------+
        | Space: | O(1)                      |
        +--------+---------------------------+

        :parameter item: the item to check membership of
        :returns: ``True`` if the item is in the left subtree, else ``False``
        """
        if self.is_left_empty():
            return False
        return self._left.contains(item)

    def right_contains(self, item: Item) -> bool:
        """
        Check if the right subtree contains the given item.

        +--------+----------------------------+
        | Time:  | O(self.get_right_length()) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter item: the item to check membership of
        :returns: ``True`` if the item is in the right subtree, else ``False``
        """
        if self.is_right_empty():
            return False
        return self._right.contains(item)

    def contains(self, item: Item) -> bool:
        """
        Check if this subtree contains the given item.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :parameter item: the item to check membership of
        :returns: ``True`` if the item is in the subtree, else ``False``
        """
        raise NotImplementedError

    def is_root(self) -> bool:
        """
        Check if this subtree has no parent.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if there's no parent, else ``False``
        """
        return self._parent is None

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

    def get_item(self) -> Item:
        """
        Get the root item in this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the item
        """
        return self._item

    def get_parent(self) -> Optional["BinarySubtree[Item]"]:
        """
        Get the parent subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the parent
        """
        return self._parent

    def get_left(self) -> Optional["BinarySubtree[Item]"]:
        """
        Get the left subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the left subtree
        """
        return self._left

    def get_right(self) -> Optional["BinarySubtree[Item]"]:
        """
        Get the right subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the right subtree
        """
        return self._right

    def get_level(self) -> int:
        """
        Get the level of this subtree.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the level
        """
        raise NotImplementedError

    def get_length(self) -> int:
        """
        Get the number of items in this subtree.

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
        Get the number of levels below the root of this subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the height
        """
        return self._height

    def get_left_length(self) -> int:
        """
        Get the number of items in the left subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the left subtree length
        """
        if self.is_left_empty():
            return 0
        return self._left.get_length()

    def get_right_length(self) -> int:
        """
        Get the number of items in the right subtree.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the right subtree length
        """
        if self.is_right_empty():
            return 0
        return self._right.get_length()

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
        return self._left.get_height()

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
        return self._right.get_height()

    def _calculate_length(self) -> int:
        """
        Calculate the length based on the subtrees' lengths.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        raise NotImplementedError

    def _calculate_height(self) -> int:
        """
        Calculate the height based on the subtrees' heights.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the height
        """
        raise NotImplementedError

    def _update_length(self) -> None:
        """
        Update the length of this subtree and its ancestors.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+
        """
        self._length = self._calculate_length()
        if not self.is_root():
            self._parent._update_length()

    def _update_height(self) -> None:
        """
        Update the height of this subtree and its ancestors.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+
        """
        old_height = self._height
        self._height = self._calculate_height()
        if not self.is_root() and old_height != self._height:
            self._parent._update_height()

    def set_item(self, new_item) -> None:
        """
        Set this subtree's root item to be the one given.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter new_item: the new item
        """
        self._item = new_item

    def insert_left(self, new_left: "BinarySubtree[Item]") -> None:
        """
        Insert the given subtree as the left child of this one.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :parameter new_left: the new left subtree
        :raises ValueError: if there's already a left subtree or ``new_left`` has a parent
        """
        raise NotImplementedError

    def insert_right(self, new_right: "BinarySubtree[Item]") -> None:
        """
        Insert the given subtree as the right child of this one.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :parameter new_right: the new right subtree
        :raises ValueError: if there's already a right subtree or ``new_right`` has a parent
        """
        raise NotImplementedError

    def remove_left(self) -> "BinarySubtree[Item]":
        """
        Remove and return the left subtree.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the old left subtree
        :raises ValueError: if there is no left subtree
        """
        raise NotImplementedError

    def remove_right(self) -> "BinarySubtree[Item]":
        """
        Remove and return the right subtree.

        +--------+---------------------+
        | Time:  | O(self.get_level()) |
        +--------+---------------------+
        | Space: | O(1)                |
        +--------+---------------------+

        :returns: the old right subtree
        :raises ValueError: if there is no right subtree
        """
        raise NotImplementedError

    def pre_iterator(self) -> Iterator[Item]:
        """
        Get a pre-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, root-left-right
        """
        raise NotImplementedError

    def iterator(self) -> Iterator[Item]:
        """
        Get an in-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, left-root-right
        """
        raise NotImplementedError

    def post_iterator(self) -> Iterator[Item]:
        """
        Get a post-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, left-right-root
        """
        raise NotImplementedError

    def reverse_pre_iterator(self) -> Iterator[Item]:
        """
        Get a reverse pre-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, root-right-left
        """
        raise NotImplementedError

    def reverse_iterator(self) -> Iterator[Item]:
        """
        Get a reverse in-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, right-root-left
        """
        raise NotImplementedError

    def reverse_post_iterator(self) -> Iterator[Item]:
        """
        Get a reverse post-order iterator over the items in this subtree.

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(1)                 |
        +--------+----------------------+

        :returns: an iterator over the subtree's items, right-left-root
        """
        raise NotImplementedError
