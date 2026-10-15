from __future__ import annotations
from typing import Any

class Node:
    """Represents a node"""
    __slots__ = ['_value', '_next']
    def __init__(self, value: Any, next_node: 'Node' | None = None):
        self._value = value
        self._next = next_node
    @property
    def value(self):
        """Returns a value"""
        return self._value
    @value.setter
    def value(self, value: Any):
        self._value = value
    @property
    def next(self):
        """Returns a next node"""
        return self._next
    @next.setter
    def next(self, next_node: Node | None):
        self._next = next_node
