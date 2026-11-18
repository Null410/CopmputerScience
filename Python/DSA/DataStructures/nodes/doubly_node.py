from __future__ import annotations
from typing import Any
from nodes.node import BaseNode

class DoublyNode(BaseNode['DoublyNode']):
    """Represents a doubly node"""
    __slots__ = ('_prev',)

    _next: 'DoublyNode | None'
    _prev: 'DoublyNode | None'

    def __init__(self, value: Any):
        self._prev = None
        super().__init__(value)
    @property
    def prev(self):
        """Returns the previous node"""
        return self._prev
    @prev.setter
    def prev(self, prev_node: 'DoublyNode | None'):
        self._prev = prev_node
