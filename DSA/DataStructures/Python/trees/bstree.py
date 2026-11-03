from typing import Any
from trees.base_tree import BaseTree
from nodes.bitree_node import TreeKey
from nodes.bitree_val_node import BiTreeValNode

class DuplicateKeyError(Exception):
    """Error: duplicate keys"""
    def __init__(self, key: TreeKey, when: str):
        self.key = key
        super().__init__(f"[{when}]: The key ({self.key}) is already in the tree!")

class NotFoundKeyError(Exception):
    """Error: key is not found"""
    def __init__(self, key: TreeKey, when: str):
        self.key = key
        super().__init__(f"[{when}]: The key ({self.key}) is not found!")

class BSTree(BaseTree):
    """Represents Binary Search Tree"""

    def insert(self, key: TreeKey, value: Any):
        """Insert the value with the key into the tree. Forbids duplicate keys."""
        new_node = BiTreeValNode(key, value)
        if self.is_empty():
            self._root = new_node
        else:
            node = self._root
            while node:
                if new_node.key == node.key:
                    raise DuplicateKeyError(new_node.key, self.insert.__name__)
                parent = node
                node = node.right if new_node.key > node.key else node.left
            if new_node.key > parent.key:
                parent.right = new_node
            else:
                parent.left = new_node
        self._count += 1

    def get(self, key: TreeKey) -> Any:
        """Finds and returns a value by the key"""
        node: BiTreeValNode = BaseTree._find_node(self._root, key)
        if node is None:
            raise NotFoundKeyError(key, self.get.__name__)
        return node.value
