from collections.abc import Iterable
from typing import Protocol, TypeVar

class Comparable(Protocol):
    """Comparable Protocol"""
    def __lt__(self, other) -> bool:
        pass
    def __le__(self, other) -> bool:
        pass
    def __gt__(self, other) -> bool:
        pass

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

def __bubble(arr: list[T]):
    n = len(arr)
    while n > 1:
        border = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                border = i + 1
        n = border

def bubble_sort(iterable: Iterable[T]) -> list[T]:
    """Bubble sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    __bubble(arr)
    return arr

def cocktail_sort(iterable: Iterable[T]) -> list[T]:
    """Cocktail sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    left = 0
    right = len(arr) - 1
    while left < right:
        border = left
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                border = i
        #Optional if block
        if border == left:
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
        if i == 0 or arr[i - 1] <= arr[i]:
            i = j
            j += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
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

def quick_sort_hoare(iterable: Iterable[T]) -> list[T]:
    """Quick sort (Hoare scheme). Returns a new sorted list[T]."""
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

def quick_sort_lomuto(iterable: Iterable[T]) -> list[T]:
    """Quick sort (Lomuto scheme, by first). Returns a new sorted list[T]."""
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

def merge_sort(iterable: Iterable[T]) -> list[T]:
    """Merge sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)

    def merge(left: list[T], right: list[T]) -> list[T]:
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    def divide_sort(arr: list[T]) -> list[T]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide_sort(arr[:mid])
        right = divide_sort(arr[mid:])
        return merge(left, right)

    return divide_sort(arr)

#I like this one more than comb_same_sort
def comb_sort(iterable: Iterable[T]) -> list[T]:
    """Comb sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)

    f = 1.247331
    def next_step(step):
        return int(step / f)

    #comb
    step = next_step(len(arr))
    while step > 1:
        for i in range(len(arr) - step):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
        step = next_step(step)

    #bubble
    __bubble(arr)
    return arr

#Same to comb_sort
def comb_same_sort(iterable: Iterable[T]) -> list[T]:
    """Comb sort (same to comb_sort). Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)

    n = len(arr)
    if n <= 1:
        return arr

    f = 1.247331
    def next_step(step):
        result = int(step / f)
        return 1 if result <= 1 else result

    step = next_step(n)
    while step >= 1:
        border = 0
        for i in range(n - step):
            if arr[i] > arr[i + step]:
                border = i + step
                arr[i], arr[border] = arr[border], arr[i]
        if step == 1:
            if border <= 1:
                break
            continue
        step = next_step(step)
    return arr

def shell_sort(iterable: Iterable[T]) -> list[T]:
    """Shell sort. Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    def next_step(step):
        return step // 2
    step = next_step(len(arr))
    while step > 0:
        for i in range(step, len(arr)):
            item = arr[i]
            j = i - step
            while j >= 0 and arr[j] > item:
                arr[j + step] = arr[j]
                j -= step
            arr[j + step] = item
        step = next_step(step)
    return arr

def shell_knuth_sort(iterable: Iterable[T]) -> list[T]:
    """Shell sort (Knuth sequence). Returns a new sorted list[T]."""
    arr: list[T] = list(iterable)
    step = 1
    while step < len(arr) // 3:
        step = step * 3 + 1
    print(step)
    while step > 0:
        for i in range(step, len(arr)):
            item = arr[i]
            j = i
            while j >= step and arr[j - step] > item:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = item
        step = (step - 1) // 3
    return arr
