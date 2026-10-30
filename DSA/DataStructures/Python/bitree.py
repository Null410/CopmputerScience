from typing import Generator
from nodes.bitree_node import BiTreeNode, TreeKey
from queue_ import Queue

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

    @staticmethod
    def __find_min(node: BiTreeNode) -> BiTreeNode:
        min_node = None
        while node:
            min_node = node
            node = node.left
        return min_node

    def delete(self, key: TreeKey):
        """Deletes a node with the specified key from the tree (the first one finded)"""
        def delete_node(node: BiTreeNode, key: TreeKey):
            find_node = False
            if node is None:
                return find_node, None
            if key == node.key:
                find_node = True
                no_l = node.left is None
                no_r = node.right is None
                if no_l and no_r:
                    return find_node, None
                if no_l:
                    return find_node, node.right
                if no_r:
                    return find_node, node.left
                min_right_node = BiTree.__find_min(node.right)
                node.key = min_right_node.key
                _, node.right = delete_node(node.right, min_right_node.key)
            elif key > node.key:
                find_node, node.right = delete_node(node.right, key)
            else:
                find_node, node.left = delete_node(node.left, key)
            return find_node, node

        find_node, self._root = delete_node(self._root, key)
        if find_node:
            self._count -= 1
        return find_node

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

    @property
    def bfs(self) -> Generator[TreeKey, None, None]:
        """Returns a generator for BFS"""
        if self.is_empty():
            return
        parent_ = Queue()
        parent_.push(self._root)
        child_ = Queue()
        while not parent_.is_empty():
            node: BiTreeNode = parent_.pop()
            if node.left:
                child_.push(node.left)
            if node.right:
                child_.push(node.right)
            yield node.key
            if parent_.is_empty():
                parent_, child_ = child_, parent_

    def __raise_if_empty(self):
        if self.is_empty():
            raise IndexError("BiTree is empty")

    def get_min(self) -> TreeKey:
        """Returns the minimum key"""
        self.__raise_if_empty()
        return BiTree.__find_min(self._root).key

    def get_max(self) -> TreeKey:
        """Returns the maximum key"""
        self.__raise_if_empty()
        node = self._root
        while node.right:
            node = node.right
        return node.key

    def get_key_depth(self, key: TreeKey) -> int:
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

    def get_depth_rec(self) -> int:
        """
        Returns the tree depth (recursive).
        If the tree is empty, returns -1.
        """
        def get_depth(node:BiTreeNode) -> int:
            if node is None:
                return -1
            return 1 + max(get_depth(node.left), get_depth(node.right))
        return get_depth(self._root)
