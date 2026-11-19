from typing import Any
from nodes.bitree_node import BiTreeNode, Key

#! Will be changed with TreeKey
class BiTreeValNode(BiTreeNode):
    """Represents a node of a binary tree with a key and a value"""
    __slots__ = ('_value',)
    def __init__(self, key: Key, value: Any):
        self._value = value
        super().__init__(key)
    @property
    def value(self):
        """Returns the value"""
        return self._value
    @value.setter
    def value(self, value: Any):
        self._value = value
