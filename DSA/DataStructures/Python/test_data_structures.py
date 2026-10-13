import pytest
from list import LinkedList

@pytest.mark.parametrize("values", [
    [1],
    [1, [2, 3]],
    ["1", 2, (3, 4)]
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

@pytest.mark.parametrize("value", [
    1,
    "1",
    [1 , 2, 3],
    (1, 2, 3)
])
def test_list_from_values_for_one_value(value):
    """Tests for creating a list from *args with only one argument"""
    list_ = LinkedList.from_values(value)
    assert list_.length == 1 and all(l == value for l in list_)

@pytest.mark.parametrize("args", [
    (1, [2, 3]),
    ("1", 2, (3, 4))
])
def test_list_from_values(args):
    """Tests for creating a list from *args"""
    list_ = LinkedList.from_values(*args)
    assert list_.length == len(args) and all(l == arg for l, arg in zip(list_, args))

@pytest.mark.parametrize("iterable", [
    [1, 2 , 3],
    [1, [2, 3]],
    (1, "2", [2, 3])
])
def test_list_from_iterable(iterable):
    """Tests for creating a list from iterable"""
    list_ = LinkedList.from_iterable(iterable)
    assert list_.length == len(iterable) and all (l == i for l, i in zip(list_, iterable))
