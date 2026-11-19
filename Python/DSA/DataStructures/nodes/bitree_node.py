from typing import Protocol, Self, Any
from abc import ABC
class Key(Protocol):
    """Key Protocol"""
    def __eq__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

class BiTreeNode(ABC):
    """Represents a node of a binary tree with a key"""
    __slots__ = ('_key', '_left', '_right')

    _left: Self | None
    _right: Self | None

    def __init__(self, key: Key):
        self._key = key
        self._left = self._right = None
    @property
    def key(self):
        """Returns the key"""
        return self._key
    @key.setter
    def key(self, key: Key):
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
