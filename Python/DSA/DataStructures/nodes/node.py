from typing import Any, Self
class Node:
    """Represents a node"""
    __slots__ = ('_value', '_next')

    _next: Self | None

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
    def next(self, next_node: Self | None):
        self._next = next_node
