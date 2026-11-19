from typing import Any, Self
from nodes.node import Node

class DoublyNode(Node):
    """Represents a doubly node"""
    __slots__ = ('_prev',)

    _prev: Self | None

    def __init__(self, value: Any):
        self._prev = None
        super().__init__(value)
    @property
    def prev(self):
        """Returns the previous node"""
        return self._prev
    @prev.setter
    def prev(self, prev_node: Self | None):
        self._prev = prev_node
