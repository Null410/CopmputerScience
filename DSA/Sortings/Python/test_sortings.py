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
    sortings.dwarf_sort,
    sortings.selection_sort,
    sortings.quick_sort,
    sortings.quick_sort_by_first,
    sortings.merge_sort,
    sortings.comb_sort,
    sortings.comb_same_sort,
    sortings.shell_sort
]

LENS: Final = [
    100,
    2,
    1,
    0
]

def is_sorted(arr: list[int]) -> bool:
    """Checks whether the list is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def get_random_unsorted_list(lenght: int, start: int = -100, stop: int = 100) -> list[int]:
    """Returns a list[int] of random unsorted elements from the range: [start; stop]"""
    def get_random_list(): 
        return [random.randint(start, stop) for _ in range(lenght)]
    rand_arr = get_random_list()
    if lenght < 2:
        return rand_arr
    while is_sorted(rand_arr):
        rand_arr = get_random_list()
    return rand_arr

@pytest.mark.parametrize("func_sort, lenght",
        list(product(SORTS, LENS)),
        ids=[f"{func_sort.__name__}_{lenght}" for func_sort, lenght in product(SORTS, LENS)])
def test_sorts(func_sort: Callable, lenght: int):
    """Sorting tests"""
    rand_arr = get_random_unsorted_list(lenght)
    assert is_sorted(func_sort(rand_arr))

@pytest.mark.parametrize("func_sort, lenght",
        list(product(SORTS, LENS)),
        ids=[f"{func_sort.__name__}_{lenght}_sorted" for func_sort, lenght in product(SORTS, LENS)])
def test_sorts_when_sorted(func_sort: Callable, lenght:int):
    """Sorting tests for sorted values"""
    sorted_arr = list(range(lenght))
    assert is_sorted(func_sort(sorted_arr))
