from __future__ import annotations
from typing import Any

class DoublyNode:
    """Represents a doubly node"""
    __slots__ = ['_value', '_next', '_prev']
    def __init__(self, value: Any):
        self._value = value
        self._next = None
        self._prev = None
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
    def next(self, next_node: 'DoublyNode' | None):
        self._next = next_node
    @property
    def prev(self):
        """Returns a previous node"""
        return self._prev
    @prev.setter
    def prec(self, prev_node: 'DoublyNode' | None):
        self._prev = prev_node
