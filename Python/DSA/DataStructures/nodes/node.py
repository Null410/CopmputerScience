from __future__ import annotations
from typing import Any, TypeVar

NodeT = TypeVar("NodeT", bound='Node')

class Node:
    """Represents a node"""
    __slots__ = ('_value', '_next')

    _next: 'Node | None'

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
    def next(self, next_node: 'Node | None'):
        self._next = next_node
