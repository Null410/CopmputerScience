from typing import TypeVar, Generator
from queue_ import Queue
from nodes.bitree_node import TreeKey, BiTreeNode

T = TypeVar("T", bound=BiTreeNode)

class BaseTree:
    """Represents a basic binary tree"""
    def __init__(self):
        self._root: T = None
        self._count = 0

    @property
    def count(self):
        """Returns the number of nodes"""
        return self._count

    def is_empty(self):
        """Returns True if tree is empty and False if not"""
        return self._root is None

    @staticmethod
    def _find_node(root: T, key: TreeKey) -> T:
        while root:
            if key == root.key:
                return root
            root = root.right if key > root.key else root.left
        return None

    def find(self, key: TreeKey) -> bool:
        """Returns True if the key is in the tree and False if not"""
        return not BaseTree._find_node(self._root, key) is None

    @staticmethod
    def _find_min(node: T) -> T:
        min_node = None
        while node:
            min_node = node
            node = node.left
        return min_node

    def delete(self, key: TreeKey):
        """
        Deletes a node with the specified key from the tree.
        If duplicate keys are allowed, deletes the first one found.
        """
        def delete_node(node: T, key: TreeKey):
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
                min_right_node = BaseTree._find_min(node.right)
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
        def preorder(node: T):
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
            node: T = parent_.pop()
            if node.left:
                child_.push(node.left)
            if node.right:
                child_.push(node.right)
            yield node.key
            if parent_.is_empty():
                parent_, child_ = child_, parent_

    def _raise_if_empty(self):
        if self.is_empty():
            raise IndexError("BiTree is empty")

    def get_depth_rec(self) -> int:
        """
        Returns the tree depth (recursive).
        If the tree is empty, returns -1.
        """
        def get_depth(node: T) -> int:
            if node is None:
                return -1
            return 1 + max(get_depth(node.left), get_depth(node.right))
        return get_depth(self._root)
