from itertools import product
from collections.abc import Sequence
from typing import Final, Callable
import pytest
from linked_list import LinkedList
from linked_list_pro import LinkedListPro
from stack import Stack
from queue_ import Queue

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

#LinkedList

@pytest.mark.parametrize("values",
    VALUES,
    ids=[str(value) for value in VALUES])
def test_list_push(values):
    """Linked list PUSH tests"""
    list_ = LinkedList()
    for v in values:
        list_.push(v)
    assert compare_sequences(list_, values)

def get_default_list(length: int) -> LinkedList:
    """Return a default linked list"""
    list_ = LinkedList()
    for i in range(length):
        list_.push(i)
    return list_

@pytest.mark.parametrize("length",[
    0,
    10
],
ids = ['0', '10'])
def test_list_length(length):
    """List length tests"""
    list_ = get_default_list(length)
    assert list_.length == length

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
    list_ = get_default_list(length)
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
    list_ = get_default_list(length)
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

@pytest.mark.parametrize("iterable", [
    [],
    [1, 2 , 3],
    [1, [2, 3]],
    (1, "2", [2, 3]),
    "12345"
])
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
def test_list_from_iter_values(args_with_expected, from_iter_func: Callable):
    """Tests for LinkedList.from_iter_values (and alternatives)"""
    args = args_with_expected[0]
    expected = args_with_expected[1]
    list_: LinkedListPro = from_iter_func(*args)
    assert compare_sequences(list_, expected)

#Stack

@pytest.mark.parametrize("values", VALUES)
def test_stack_push(values):
    """Stack PUSH tests"""
    stack = Stack()
    for v in values:
        stack.push(v)
    assert compare_sequences(stack, values[::-1])

@pytest.mark.parametrize("method", [
    Stack.pop,
    Stack.peek
])
def test_stack_pop_peek_index_error(method):
    """Stack IndexError tests (pop, peek)"""
    stack = Stack()
    with pytest.raises(IndexError):
        method(stack)

#Queue

@pytest.mark.parametrize("values", VALUES)
def test_queue_push(values):
    """Queue PUSH tests"""
    queue = Queue()
    for value in values:
        queue.push(value)
    assert compare_sequences(queue, values)

@pytest.mark.parametrize("method", [
    Queue.pop,
    Queue.peek
])
def test_queue_pop_peek_index_error(method):
    """Quequ IndexError tests (pop, peek)"""
    queue = Queue()
    with pytest.raises(IndexError):
        method(queue)

#Stack and Queue

def get_stack(arr: list) -> Stack:
    """
    Returna a new stack from a list.
    The order of thr elements is preserved.
    Example:
        Input: [1, 2, 3]
        Output: 1 -> 2 -> 3
    """
    stack = Stack()
    for a in arr[::-1]:
        stack.push(a)
    return stack

def get_queue(arr: list) -> Stack:
    """Returna a new queue from a list."""
    queue = Queue()
    for a in arr:
        queue.push(a)
    return queue

GET_FUNCS = [
    get_stack,
    get_queue
]

@pytest.mark.parametrize("values, get_func",
    list(product(VALUES, GET_FUNCS)),
    ids = [f"{get_func.__name__}_{value}" for value, get_func in product(VALUES, GET_FUNCS)])
def test_stask_queue_pop(values, get_func):
    """Stack and Queue POP tests"""
    struct = get_func(values)
    value = struct.pop()
    assert value == values[0] and compare_sequences(struct, values[1:])

@pytest.mark.parametrize("values, get_func",
    list(product(VALUES, GET_FUNCS)),
    ids = [f"{get_func.__name__}_{value}" for value, get_func in product(VALUES, GET_FUNCS)])
def test_stask_queue_peek(values, get_func):
    """Stack and Queue PEEK tests"""
    struct = get_func(values)
    value = struct.peek()
    assert value == values[0] and len(struct) == len(values)
