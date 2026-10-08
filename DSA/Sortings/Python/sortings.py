from collections.abc import Iterable
from typing import Protocol, TypeVar

def Comparable(Protocol):
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...

T = TypeVar('T', bound = Comparable)

def bubble_simple_sort(iterable: Iterable[T]) -> list[T]:
    """Simple bubble sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort(iterable: Iterable[T]) -> list[T]:
    """Bubble sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    n = len(arr)
    while n > 1:
        border = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                border = i + 1
        n = border
    return arr

def cocktail_sort(iterable: Iterable[T]) -> list[T]:
    """Cocktail sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    left = 0
    right = len(arr) - 1
    while left < right:
        swapped = False
        border = left
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                border = i
        if not swapped:
            break
        right = border

        for j in range(right, left, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                border = j
        left = border
    return arr
