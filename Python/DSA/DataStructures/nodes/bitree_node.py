from typing import Self, Any
from abc import ABC

class BiTreeNode(ABC):
    """Represents a node of a binary tree with a key"""
    __slots__ = ('_key', '_left', '_right')

    _left: Self | None
    _right: Self | None

    def __init__(self, key: Any):
        self._key = key
        self._left = self._right = None
    @property
    def key(self):
        """Returns the key"""
        return self._key
    @key.setter
    def key(self, key: Any):
        self._key = key
    @property
    def left(self):
        """Returns the left node"""
        return self._left
    @left.setter
    def left(self, left: Self | None):
        self._left = left
    @property
    def right(self):
        """Returns the right node"""
        return self._right
    @right.setter
    def right(self, right: Self | None):
        self._right = right
