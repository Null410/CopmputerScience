from collections.abc import Iterable
from typing import Protocol, TypeVar

def Comparable(Protocol):
    #def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
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

def insertion_sort(iterable: Iterable[T]) -> list[T]:
    """Insertion sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    for i in range(1, len(arr)):
        item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item
    return arr

def dwarf_sort(iterable: Iterable[T]) -> list[T]:
    """Dwarf sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    i = 1
    j = i + 1
    while i < len(arr):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
        else:
            # if arr[i - 1] <= arr[i]
            i = j
            j += 1
    return arr

def selection_sort(iterable: Iterable[T]) -> list[T]:
    """Selection sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(iterable: Iterable[T]) -> list[T]:
    """Quick sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)

    def partition(arr: list[T], l: int, r: int) -> int:
        pivot = arr[(r + l) // 2]
        i = l
        j = r
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return j

    def quick(arr: list[T], l: int, r: int):
        if l >= r:
            return
        p = partition(arr, l, r)
        quick(arr, l, p)
        quick(arr, p + 1, r)
    quick(arr, 0, len(arr) - 1)
    return arr

def quick_sort_by_first(iterable: Iterable[T]) -> list[T]:
    """Quick sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)

    def partition(arr: list[T], l: int, r: int) -> int:
        pivot = arr[l]
        p = l
        for i in range(l + 1, r + 1):
            if arr[i] <= pivot:
                p += 1
                arr[i], arr[p] = arr[p], arr[i]
        arr[l], arr[p] = arr[p], arr[l]
        return p

    def quick(arr: list[T], l: int, r: int):
        if l >= r:
            return
        p = partition(arr, l, r)
        quick(arr, l, p - 1)
        quick(arr, p + 1, r)

    quick(arr, 0, len(arr) - 1)
    return arr
