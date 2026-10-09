from typing import Callable, Final
from itertools import product
import random
import pytest
import sortings

SORTS: Final = [
    sortings.bubble_simple_sort,
    sortings.bubble_sort,
    sortings.cocktail_sort,
    sortings.insertion_sort,
    sortings.dwarf_sort
]

LENS: Final = [
    100,
    2,
    1,
    0
]

def get_random_list(lenght: int, start: int = -100, stop: int = 100) -> list[int]:
    """Returns a list[int] of random elements from the range: [start; stop]"""
    return [random.randint(start, stop) for _ in range(lenght)]

@pytest.mark.parametrize("func_sort, lenght",
        list(product(SORTS, LENS)),
        ids=[f"{func_sort.__name__}_{lenght}" for func_sort, lenght in product(SORTS, LENS)])
def test_sorts(func_sort: Callable, lenght: int):
    """Sorting tests"""
    rand_arr = get_random_list(lenght)
    assert func_sort(rand_arr) == sorted(rand_arr)

@pytest.mark.parametrize("func_sort, lenght",
        list(product(SORTS, LENS)),
        ids=[f"{func_sort.__name__}_{lenght}_sorted" for func_sort, lenght in product(SORTS, LENS)])
def test_sorts_when_sorted(func_sort: Callable, lenght:int):
    """Sorting tests for sorted values"""
    sorted_arr = list(range(lenght))
    assert func_sort(sorted_arr) == sorted_arr
