from typing import Callable
import random
import pytest
import sortings

def get_random_list(len: int, start: int = -100, stop: int = 100) -> list[int]:
    """Returns a list[int] of random elements from the range: [start; stop]"""
    return [random.randint(start, stop) for _ in range(len)]

@pytest.mark.parametrize("func_sort", [
    sortings.bubble_simple_sort,
    sortings.bubble_sort
], ids=[
    "test_bubble_simple_sort",
    "test_bubble_surt"
])
def test_sorts(func_sort: Callable):
    """Sorting tests"""
    n = 100
    rand_arr = get_random_list(n)
    assert func_sort(rand_arr) == sorted(rand_arr)
