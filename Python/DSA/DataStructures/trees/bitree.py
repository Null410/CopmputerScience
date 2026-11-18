from nodes.bitree_node import BiTreeNode, Key
from trees.base_tree import BaseTree

#! Will be changed with TreeKey
class BiTree(BaseTree[BiTreeNode]):
    """Represents a binary tree"""
    _root: BiTreeNode | None

    def insert(self, key: Key):
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

    def get_min(self) -> Key:
        """Returns the minimum key"""
        root = self._raise_if_empty()
        return BiTree._find_min(root).key

    def get_max(self) -> Key:
        """Returns the maximum key"""
        node = self._raise_if_empty() # _root
        while node.right:
            node = node.right
        return node.key

    def get_key_depth(self, key: Key) -> int:
        """
        Returns the key depth (the first one found).
        The root depth is 0.
        If the key is not found, returns -1.
        """
        depth = -1
        node = self._root
        while node:
            depth += 1
            if key == node.key:
                return depth
            node = node.right if key > node.key else node.left
        return -1

    def get_key_count(self, key: Key):
        """Returns the key count"""
        count = 0
        node = self._root
        while node:
            node = self._find_node(node, key)
            if node is None:
                break
            count += 1
            node = node.left
        return count
