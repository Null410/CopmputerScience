from itertools import product
from typing import Final, Callable, Iterable
import random
import pytest
from trees.bitree import BiTree

#BiTree

def get_bitree(values: Iterable, cls: type = int):
    """Returns a new BiTree of values"""
    tree = BiTree()
    for v in values:
        tree.insert(cls(v))
    return tree

class KeyTest:
    """Represents a key suitable for the tree key protocol"""
    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        if isinstance(other, KeyTest):
            return self._value == other._value
        return self._value == other
    def __gt__(self, other):
        if isinstance(other, KeyTest):
            return self._value > other._value
        return self._value > other

    def __mul__(self, other):
        if isinstance(other, KeyTest):
            return KeyTest(self._value * other._value)
        return KeyTest(self._value * other)
    def __str__(self):
        return f"{KeyTest.__name__}({self._value})"

@pytest.mark.parametrize("key", [
    1,
    1.0,
    "key",
    [],
    [1],
    (1, 2),
    KeyTest(1)
],
ids=type)
def test_bitree_insert_keys_type(key):
    """Tests BiTree keys type (when insert)"""
    tree = BiTree()
    tree.insert(key)
    tree.insert(key)
    tree.insert(key * 2)
    assert tree.count == 3

@pytest.mark.parametrize("cls",[
    int,
    float,
    str,
    KeyTest
],
ids=lambda x: x.__name__)
def test_bitree_find(cls):
    """Test BiTree: (not) find"""
    n = 10
    list_ = list(range(n))
    random.shuffle(list_)
    tree = get_bitree(list_, cls)
    assert tree.find(cls(n // 2)) and not tree.find(cls(n * 2))

TREE_VALUES_DFS: Final = [
    ([], []),
    ([5, 3, 2, 4, 8, 10], [5, 3, 2, 4, 8, 10]),
    ([10, 15, 4, 11], [10, 4, 15, 11])
]

@pytest.mark.parametrize("values, dfs", TREE_VALUES_DFS, ids=str)
def test_bitree_dfs(values, dfs):
    """Tests Bitree: DFS (preorder, recursive)"""
    tree = get_bitree(values, int)
    assert all(tree_dfs == exp_dfs for tree_dfs, exp_dfs in zip(tree.dfs_rec, dfs))

TREE_VALUES_BFS: Final = [
    ([], []),
    ([5, 3, 2, 4, 8, 10, 7], [5, 3, 8, 2, 4, 7, 10]),
    ([10, 15, 4, 11, 3, 16], [10, 4, 15, 3, 11, 16])
]
@pytest.mark.parametrize("values, bfs", TREE_VALUES_BFS, ids=str)
def test_bitree_bfs(values, bfs):
    """Tests Bitree: BFS"""
    tree = get_bitree(values, int)
    assert all(tree_bfs == exp_bfs for tree_bfs, exp_bfs in zip(tree.bfs, bfs))

@pytest.mark.parametrize("values, del_values, result_bfs", [
    ([], [0], []),
    ([3, 2, 4], [3], [4, 2]),
    ([3, 2, 2, 4, 4], [2, 4], [3, 2, 4]),
    ([5, 3, 7, 4, 6], [3, 7], [5, 4, 6]),
    ([0], [0], []),
    ([0, -1, 1], [0, -1, 1], []),
    ([3, 1, 1, 5, 5, 4, 3], [1, 3, 5], [4, 3, 5, 1]),
    ([3, 2, 4], [1, -1], [3, 2, 4]),
    ([5, 3, 2, 4, 8, 10, 7], [3, 8], [5, 4, 10, 2, 7])
],
ids = [
    "when_empty",
    "when_root",
    "when_leaf",
    "when_one_child",
    "when_only_one",
    "delete_all",
    "duplicate_keys",
    "when_is_missing",
    "common"
])
def test_bitree_delete(values, del_values, result_bfs):
    """Tests BiTree: delete"""
    tree = get_bitree(values, int)
    for dv in del_values:
        tree.delete(dv)
    assert tree.count == len(result_bfs) and all(tree_bfs == exp_bfs for tree_bfs, exp_bfs in zip(tree.bfs, result_bfs))

@pytest.mark.parametrize("values, func",
    list(product([
        [1],
        [2, 1, 3],
        [5, 4, 6, 3, 5, 6, 7],
        [1, 2, 3],
        [3, 2, 1]
    ],[
        BiTree.get_min,
        BiTree.get_max
    ])),
    ids=lambda x: x.__name__ if isinstance(x, Callable) else str(x))
def test_bitree_min(values, func):
    """Tests BiTree: min/max"""
    tree = get_bitree(values)
    exp_func = min if func is BiTree.get_min else max
    assert func(tree) == exp_func(values)

@pytest.mark.parametrize("func",[
    BiTree.get_min,
    BiTree.get_max
])
def test_bitree_index_error(func):
    """Tests BiTree: IndexError"""
    tree = BiTree()
    with pytest.raises(IndexError):
        func(tree)

@pytest.mark.parametrize("values, key, depth",[
    ([], 0, -1),
    ([0], 1, -1),
    ([0], 0, 0),
    ([2, 1, 3], 3, 1),
    ([2, 1, 3, 0], 0 , 2),
    ([2, 1, 3, 0, 0, 0], 0, 2)
],
ids = [
    "empty_tree_(-1)",
    "only_root_(-1)",
    "only_root_(0)",
    "left_(1)",
    "right_(2)",
    "several (2)"
])
def test_bitree_key_depth(values, key, depth):
    """Tests BiTree: key depth"""
    tree = get_bitree(values)
    assert tree.get_key_depth(key) == depth

@pytest.mark.parametrize("values, depth", [
    ([], -1),
    ([0], 0),
    ([2, 1, 3], 1),
    ([2, 1, 3, 0, -1], 3),
    ([2, 1, 5, 6], 2)
],
ids = lambda x: f"({x})" if isinstance(x, int) else str(x))
def test_bitree_depth_rec(values, depth):
    """Tests BiTree depth (recursive)"""
    tree = get_bitree(values)
    assert tree.get_depth_rec() == depth

@pytest.mark.parametrize("values, key",[
    ([], 1),
    ([0], 1),
    ([2, 1, 3], 2),
    ([2, 3, 2, 2], 2),
    ([6, 5, 4, 6], 6),
    ([6, 5, 5, 3, 5, 5, 4, 5, 6], 5)
], ids = [
    "empty_tree",
    "not_found",
    "only_root",
    "several_in_a_row",
    "several_not_in_a_row",
    "several_special"
])
def test_bitree_key_count(values: list, key):
    """Tests BiTree: key count"""
    tree = get_bitree(values)
    assert tree.get_key_count(key) == values.count(key)
