from __future__ import annotations
from typing import Protocol, TypeVar

class Key(Protocol):
    """Key Protocol"""
    def __eq__(self, other):
        pass
    def __gt__(self, other):
        pass

TreeKey = TypeVar('TreeKey', bound=Key)

class BiTreeNode:
    """Represents a node of a binary tree with immutable key"""
    __slots__ = ('_key', '_left', '_right')
    def __init__(self, key: TreeKey):
        self._key = key
        self._left = self._right = None
    @property
    def key(self):
        """Returns the key"""
        return self._key
    @property
    def left(self):
        """Returns the left node"""
        return self._left
    @left.setter
    def left(self, left: 'BiTreeNode' | None):
        self._left = left
    @property
    def right(self):
        """Returns the right node"""
        return self._right
    @right.setter
    def right(self, right: 'BiTreeNode' | None):
        self._right = right
