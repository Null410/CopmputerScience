from __future__ import annotations
from typing import Protocol, TypeVar, Generic, Any
from abc import ABC
class Key(Protocol):
    """Key Protocol"""
    def __eq__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

BiTreeNodeT = TypeVar('BiTreeNodeT', bound='BaseTreeNode[Any]')
TreeKey = TypeVar('TreeKey', bound=Key)

#! Will be changed with TreeKey
class BaseTreeNode(Generic[BiTreeNodeT], ABC):
    """Represents a base parent node for other nodes of a binary tree with a key"""
    __slots__ = ('_key', '_left', '_right')

    _left: 'BiTreeNodeT | None'
    _right: 'BiTreeNodeT | None'

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
    def left(self, left: 'BiTreeNodeT | None'):
        self._left = left
    @property
    def right(self):
        """Returns the right node"""
        return self._right
    @right.setter
    def right(self, right: 'BiTreeNodeT | None'):
        self._right = right

class BiTreeNode(BaseTreeNode['BiTreeNode']):
    """Represents a node of a binary tree with a key"""
