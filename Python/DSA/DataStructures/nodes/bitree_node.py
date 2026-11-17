from __future__ import annotations
from typing import Protocol, TypeVar

class Key(Protocol):
    """Key Protocol"""
    def __eq__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...

TreeKey = TypeVar('TreeKey', bound=Key)
BiTreeNodeT = TypeVar("BiTreeNodeT", bound='BiTreeNode')

#! Will be changed with 'Generic[TreeKey, BiTreeNodeT]'
class BiTreeNode:
    """Represents a node of a binary tree with a key"""
    __slots__ = ('_key', '_left', '_right')

    _left: 'BiTreeNode | None'
    _right: 'BiTreeNode | None'

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
    def left(self, left: 'BiTreeNode | None'):
        self._left = left
    @property
    def right(self):
        """Returns the right node"""
        return self._right
    @right.setter
    def right(self, right: 'BiTreeNode | None'):
        self._right = right
