from __future__ import annotations
from typing import Any, TypeVar, Generic
from abc import ABC

NodeT = TypeVar("NodeT", bound='BaseNode[Any]')

class BaseNode(Generic[NodeT], ABC):
    """Represents a base parent node"""
    __slots__ = ('_value', '_next')

    _next: NodeT | None

    def __init__(self, value: Any):
        self._value = value
        self._next = None
    @property
    def value(self):
        """Returns the value"""
        return self._value
    @value.setter
    def value(self, value: Any):
        self._value = value
    @property
    def next(self):
        """Returns the next node"""
        return self._next
    @next.setter
    def next(self, next_node: NodeT | None):
        self._next = next_node

class Node(BaseNode['Node']):
    """Represents a node"""
