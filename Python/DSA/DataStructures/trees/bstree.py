from typing import Any
from trees.base_tree import BaseTree
from nodes.bitree_node import Key
from nodes.bitree_val_node import BiTreeValNode

class DuplicateKeyError(Exception):
    """Error: duplicate keys"""
    def __init__(self, key: Key, when: str):
        self.key = key
        super().__init__(f"[{when}]: The key ({self.key}) is already in the tree!")

class NotFoundKeyError(Exception):
    """Error: key is not found"""
    def __init__(self, key: Key, when: str):
        self.key = key
        super().__init__(f"[{when}]: The key ({self.key}) is not found!")

class BSTree(BaseTree[BiTreeValNode]):
    """Represents Binary Search Tree"""

    def insert(self, key: Key, value: Any):
        """Insert the value with the key into the tree. Forbids duplicate keys."""
        new_node = BiTreeValNode(key, value)
        if self._root is None:
            self._root = new_node
        else:
            node = self._root
            while True:
                if new_node.key == node.key:
                    raise DuplicateKeyError(new_node.key, self.insert.__name__)
                if new_node.key > node.key:
                    if node.right is None:
                        node.right = new_node
                        break
                    node = node.right
                else:
                    if node.left is None:
                        node.left = new_node
                        break
                    node = node.left
        self._count += 1

    def get(self, key: Key) -> Any:
        """Finds and returns a value by the key"""
        node = self._find_node(self._root, key)
        if node is None:
            raise NotFoundKeyError(key, self.get.__name__)
        return node.value
