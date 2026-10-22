from itertools import product
from collections.abc import Sequence
from typing import TypeVar, Final, Callable, Iterable
import pytest
from struct_interface import BaseStruct, Struct
from linked_list import LinkedList
from linked_list_pro import LinkedListPro
from stack import Stack
from queue_ import Queue
from deque_ import Deque

def get_stack(arr: Iterable) -> Stack:
    """
    Returna a new stack from an iterable.
    The order of thr elements is preserved.
    Example:
        Input: [1, 2, 3]
        Output: 1 -> 2 -> 3
    """
    stack = Stack()
    for a in arr[::-1]:
        stack.push(a)
    return stack

BaseStructT = TypeVar('BaseStructT', bound=BaseStruct)

def get_struct_from_iterable(arr: Iterable, struct_type: type[BaseStructT]) -> BaseStructT:
    """Returna a new struct from an iterable."""
    if struct_type is Stack:
        return get_stack(arr)
    struct = struct_type()
    for a in arr:
        struct.push(a)
    return struct

def get_default_struct(length: int, struct_type: type[BaseStructT]) -> BaseStructT:
    """Return a default struct"""
    return get_struct_from_iterable(range(length), struct_type)

def compare_sequences(seq1: Sequence, seq2: Sequence):
    """Compare sequences"""
    return len(seq1) == len(seq2) and all (a1 == a2 for a1, a2 in zip(seq1, seq2))

VALUES: Final = [
    [1],
    ['1'],
    ['1', 2, '3'],
    [1, [2, 3]],
    ['1', 2, (3, 4)],
    [None]
]

#LinkedList, Stack, Queue, Deque

BASE_STRUCT_TYPES: Final[type[BaseStruct]]= [
    LinkedList,
    Stack,
    Queue,
    Deque
]

@pytest.mark.parametrize("values, struct_type",
    list(product(VALUES,  BASE_STRUCT_TYPES)),
    ids=[f"{s_type.__name__}_{value}" for value, s_type in product(VALUES,  BASE_STRUCT_TYPES)])
def test_struct_push(values, struct_type):
    """Struct PUSH tests"""
    struct = get_struct_from_iterable(values, struct_type)
    assert compare_sequences(struct, values)

LENG: Final = [
    0,
    10
]

@pytest.mark.parametrize("length, struct_type",
    list(product(LENG, BASE_STRUCT_TYPES)),
    ids = [f"{s_type.__name__}_{leng}" for leng, s_type in product(LENG,  BASE_STRUCT_TYPES)])
def test_struct_length(length, struct_type):
    """Struct length tests"""
    struct = get_default_struct(length, struct_type)
    assert len(struct) == length

#Stack, Queue, Deque

STRUCT_TYPES: Final[type[Struct]] = [
    Stack,
    Queue,
    Deque
]

@pytest.mark.parametrize("values, struct_type",
    list(product(VALUES, STRUCT_TYPES)),
    ids = [f"{s_type.__name__}_{value}" for value, s_type in product(VALUES, STRUCT_TYPES)])
def test_struct_pop(values, struct_type: type[Struct]):
    """Struct POP tests"""
    struct = get_struct_from_iterable(values, struct_type)
    value = struct.pop()
    assert value == values[0] and len(struct) == len(values) - 1 and compare_sequences(struct, values[1:])

@pytest.mark.parametrize("values, struct_type",
    list(product(VALUES, STRUCT_TYPES)),
    ids = [f"{s_type.__name__}_{value}" for value, s_type in product(VALUES, STRUCT_TYPES)])
def test_struct_peek(values, struct_type: type[Struct]):
    """Struct PEEK tests"""
    struct = get_struct_from_iterable(values, struct_type)
    value = struct.peek()
    assert value == values[0] and len(struct) == len(values) and compare_sequences(struct, values)

METHOD_NAMES: Final = [
    Struct.peek.__name__,
    Struct.pop.__name__
]

@pytest.mark.parametrize("struct_type , method_name",
    list(product(STRUCT_TYPES, METHOD_NAMES)),
    ids=[f"{s_type.__name__}_{method_name}" for s_type, method_name in product(STRUCT_TYPES, METHOD_NAMES)])
def test_struct_pop_index_error(struct_type: type[Struct], method_name):
    """Struct IndexError tests (pop, peek)"""
    struct = struct_type()
    method = getattr(struct, method_name)
    with pytest.raises(IndexError):
        _ = method()

#LinkedList

@pytest.mark.parametrize("length, idx",[
    (1, 0),
    (2, 1),
    (3, 2),
    (10, 5),
    (1, -1),
    (2, -1)
])
def test_list_getitem(length, idx):
    """List __getitem__ tests"""
    list_ = get_default_struct(length, LinkedList)
    exp = list(range(length))
    assert list_[idx] == exp[idx]

@pytest.mark.parametrize("length, idx",[
    (1, -2),
    (1, 1),
    (1, 2),
    (2, 10)
])
def test_list_getitem_index_error(length, idx):
    """List __getitem__ IndexError tests"""
    list_ = get_default_struct(length, LinkedList)
    with pytest.raises(IndexError):
        _ = list_[idx]

#LinkedListPro

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
    list_ = LinkedListPro.from_values(*args)
    assert compare_sequences(list_, args)

ITERABLE_VALUES: Final = [
    [],
    [1, 2 , 3],
    [1, [2, 3]],
    (1, "2", [2, 3]),
    "12345"
]

@pytest.mark.parametrize("iterable", ITERABLE_VALUES)
def test_list_from_iterable(iterable):
    """Tests for creating a list from iterable"""
    list_ = LinkedListPro.from_iterable(iterable)
    assert compare_sequences(list_, iterable)

ITER_FUNCS: Final = [
    LinkedListPro.from_iter_values,
    LinkedListPro.from_iter_values_alternative_1,
    LinkedListPro.from_iter_values_alternative_2
]

@pytest.mark.parametrize("iter_func", ITER_FUNCS)
def test_list_from_iter_values_when_empty(iter_func):
    """Tests for creating a list from iterable"""
    list_: LinkedListPro = iter_func()
    assert len(list_) == 0

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
def test_list_from_iter_values(args_with_expected, from_iter_func: Callable):
    """Tests for LinkedList.from_iter_values (and alternatives)"""
    args = args_with_expected[0]
    expected = args_with_expected[1]
    list_: LinkedListPro = from_iter_func(*args)
    assert compare_sequences(list_, expected)

#Deque

@pytest.mark.parametrize("values", ITERABLE_VALUES,
    ids = str)
def test_deque_reversed(values):
    """Tests for Qeque __reversed__"""
    deque = get_struct_from_iterable(values, Deque)
    assert all(d == v for d, v in zip(reversed(deque), reversed(values)))
