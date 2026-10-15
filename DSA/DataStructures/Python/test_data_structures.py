from itertools import product
from typing import Final, Callable
from linked_list import LinkedList
import pytest

@pytest.mark.parametrize("values", [
    [1],
    ['1'],
    [1, [2, 3]],
    ['1', 2, (3, 4)],
    [None]
])
def test_push(values):
    """Push method tests"""
    list_ = LinkedList()
    for v in values:
        list_.push(v)
    assert all(l == v for l, v in zip(list_, values))

def get_default_list(length: int) -> LinkedList:
    """Return a default linked list"""
    list_ = LinkedList()
    for i in range(length):
        list_.push(i)
    return list_

@pytest.mark.parametrize("length",[
    0,
    10
])
def test_list_length(length):
    """List length tests"""
    list_ = get_default_list(length)
    assert list_.length == length

@pytest.mark.parametrize("args", [
    (),
    (1,),
    (1, [2, 3]),
    ("1", 2, (3, 4)),
    ("123",),
    ([1, 2, 3],),
    ((1, 2, 3),)
])
def test_list_from_values(args):
    """Tests for creating a list from *args"""
    list_ = LinkedList.from_values(*args)
    assert list_.length == len(args) and all(l == arg for l, arg in zip(list_, args))

@pytest.mark.parametrize("iterable", [
    [],
    [1, 2 , 3],
    [1, [2, 3]],
    (1, "2", [2, 3]),
    "12345"
])
def test_list_from_iterable(iterable):
    """Tests for creating a list from iterable"""
    list_ = LinkedList.from_iterable(iterable)
    assert list_.length == len(iterable) and all (l == i for l, i in zip(list_, iterable))

ITER_FUNCS: Final = [
    LinkedList.from_iter_values,
    LinkedList.from_iter_values_alternative_1,
    LinkedList.from_iter_values_alternative_2
]

@pytest.mark.parametrize("iter_func", ITER_FUNCS)
def test_from_iter_values_when_empty(iter_func):
    """Tests for creating a list from iterable"""
    list_: LinkedList = iter_func()
    assert list_.length == 0

ARGS_WITH_EXPECTED: Final = [
    [ ( 1, ), [1] ],
    [ ( 1, [2, 3] ), [1, 2, 3] ],
    [ ( '1', 2, (3, 4) ), ['1', 2, 3, 4] ],
    [ ( '1', ), ['1'] ],
    [ ( [1, 2, 3], ), [1, 2, 3] ],
    [ ( (1, 2, 3), ), [1, 2, 3] ],
    [ ( [1, 2, 3], 4 , 5 ), [1, 2, 3 , 4, 5] ],
    [ ( [1, [2, 3]], ), [1, 2, 3] ],
    [ ( [[1], ['2', 3], [4, 5, 6, [7]], 8]), [1, '2', 3, 4, 5, 6, 7 ,8] ],
    [ ( "12345", ), ['1', '2', '3', '4', '5'] ],
    [ ( "12", "34", 5), ['1', '2', '3', '4', 5] ]
]

@pytest.mark.parametrize("args_with_expected, from_iter_func",
    list(product(ARGS_WITH_EXPECTED, ITER_FUNCS)),
    ids=[f"{f.__name__} for {a[0]}" for a, f in product(ARGS_WITH_EXPECTED, ITER_FUNCS)]
)
def test_from_iter_values(args_with_expected, from_iter_func: Callable):
    """Tests for LinkedList.from_iter_values (and alternatives)"""
    args = args_with_expected[0]
    expected = args_with_expected[1]
    list_: LinkedList = from_iter_func(*args)
    assert list_.length == len(expected) and all(l == e for l, e in zip(list_, expected))
