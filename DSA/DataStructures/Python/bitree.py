from typing import Generator
from bitree_node import BiTreeNode, TreeKey

class BiTree:
    """Represents a binary tree"""
    def __init__(self):
        self._root: BiTreeNode = None
        self._count = 0

    @property
    def count(self):
        """Returns the number of nodes"""
        return self._count

    def is_empty(self):
        """Returns True if tree is empty and False if not"""
        return self._root is None

    def insert(self, key: TreeKey):
        """Insert the key into the tree. Allows duplicate keys."""
        new_node = BiTreeNode(key)
        if self.is_empty():
            self._root = new_node
        else:
            node = self._root
            while node:
                parent = node
                node = node.right if new_node.key > node.key else node.left
            if new_node.key > parent.key:
                parent.right = new_node
            else:
                parent.left = new_node
        self._count += 1

    def find(self, key: TreeKey) -> bool:
        """Returns True if the key is in the tree and False if not"""
        node = self._root
        while node:
            if node.key == key:
                return True
            if key > node.key:
                node = node.right
            else:
                node = node.left
        return False

    def delete(self, key: TreeKey):
        """Deletes a node with the specified key from the tree"""
        raise NotImplementedError

    @property
    def dfs_rec(self) -> Generator[TreeKey, None, None]:
        """Returns a generator for recursive DFS"""
        def preorder(node: BiTreeNode):
            if node is None:
                return
            yield node.key
            yield from preorder(node.left)
            yield from preorder(node.right)
        yield from preorder(self._root)
