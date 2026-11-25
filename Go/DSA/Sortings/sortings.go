package sortings

import (
	"cmp"
	"iter"
	"slices"
)

func bubble[T any](arr []T, compare func(a, b T) int) {
	n := len(arr)
	border := 0
	for n > 1 {
		for i := 0; i < n-1; i++ {
			if compare(arr[i], arr[i+1]) > 0 {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				border = i + 1
			}
		}
		n = border
	}
}

// Bubble sort.
// Returns a new slice []T, sorted according to the comparison function.
func BubbleSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	bubble(arr, compare)
	return arr
}

// Bubble sort.
// Returns a new slice []T, sorted in ascending order.
func BubbleSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return BubbleSortFunc(seq, cmp.Compare[T])
}

// Cocktail sort.
// Returns a new slice []T, sorted according to the comparison function.
func CocktailSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	left := 0
	right := len(arr) - 1
	for left < right {
		border := 0
		for i := left; i < right; i++ {
			if compare(arr[i], arr[i+1]) > 0 {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				border = i
			}
		}
		right = border
		for j := right; j > left; j-- {
			if compare(arr[j-1], arr[j]) > 0 {
				arr[j-1], arr[j] = arr[j], arr[j-1]
				border = j
			}
		}
		left = border
	}
	return arr
}

// Cocktail sort.
// Returns a new slice []T, sorted in ascending order.
func CocktailSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return CocktailSortFunc(seq, cmp.Compare[T])
}

// Insertion sort.
// Returns a new slice []T, sorted according to the comparison function.
func InsertionSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	for i := 1; i < len(arr); i++ {
		item := arr[i]
		j := i - 1
		for j >= 0 && compare(arr[j], item) > 0 {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = item
	}
	return arr
}

// Insertion sort.
// Returns a new slice []T, sorted in ascending order.
func InsertionSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return InsertionSortFunc(seq, cmp.Compare[T])
}

// Dwarf sort.
// Returns a new slice []T, sorted according to the comparison function.
func DwarfSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	i := 1
	j := i + 1
	for i < len(arr) {
		if i == 0 || compare(arr[i-1], arr[i]) < 0 {
			i = j
			j++
		} else {
			arr[i-1], arr[i] = arr[i], arr[i-1]
			i--
		}
	}
	return arr
}

// Dwarf sort.
// Returns a new slice []T, sorted in ascending order.
func DwarfSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return DwarfSortFunc(seq, cmp.Compare)
}

// Selection sort.
// Returns a new slice []T, sorted according to the comparison function.
func SelectionSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	for i := 0; i < len(arr)-1; i++ {
		min_idx := i
		for j := i + 1; j < len(arr); j++ {
			if compare(arr[j], arr[min_idx]) < 0 {
				min_idx = j
			}
		}
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	}
	return arr
}

// Selection sort.
// Returns a mew slice []T, sorted in ascending order.
func SelectionSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return SelectionSortFunc(seq, cmp.Compare)
}

func quickSortLomutoFunc[T any](arr []T, l, r int, compare func(a, b T) int) {
	if l >= r {
		return
	}

	partition := func(arr []T, l, r int) int {
		pivot := arr[r]
		p := l - 1
		for i := l; i < r; i++ {
			if compare(arr[i], pivot) <= 0 {
				p++
				arr[i], arr[p] = arr[p], arr[i]
			}
		}
		p++
		arr[p], arr[r] = arr[r], arr[p]
		return p
	}

	p := partition(arr, l, r)
	quickSortLomutoFunc(arr, l, p-1, compare)
	quickSortLomutoFunc(arr, p+1, r, compare)
}

// Quick sort (Lomuto scheme, by last)
// Returns a new slice []T, sorted according to the comparison function.
func QuickSortLomutoFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	quickSortLomutoFunc(arr, 0, len(arr)-1, compare)
	return arr
}

// Quick sort (Lomuto scheme, by last)
// Returns a mew slice []T, sorted in ascending order.
func QuickSortLomuto[T cmp.Ordered](seq iter.Seq[T]) []T {
	return QuickSortLomutoFunc(seq, cmp.Compare)
}

func quickSortHoareFunc[T any](arr []T, l, r int, compare func(a, b T) int) {
	if l >= r {
		return
	}

	partition := func(arr []T, l, r int) int {
		pivot := arr[(l+r)/2]
		i := l
		j := r
		for i < j {
			for compare(arr[i], pivot) < 0 {
				i++
			}
			for compare(arr[j], pivot) > 0 {
				j--
			}
			if i >= j {
				break
			}
			arr[i], arr[j] = arr[j], arr[i]
			i++
			j--
		}
		return j
	}

	p := partition(arr, l, r)
	quickSortHoareFunc(arr, l, p, compare)
	quickSortHoareFunc(arr, p+1, r, compare)
}

// Quick sort (Hoare scheme)
// Returns a new slice []T, sorted according to the comparison function.
func QuickSortHoareFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	quickSortHoareFunc(arr, 0, len(arr)-1, compare)
	return arr
}

// Quick sort (Hoare scheme)
// Returns a mew slice []T, sorted in ascending order.
func QuickSortHoare[T cmp.Ordered](seq iter.Seq[T]) []T {
	return QuickSortHoareFunc(seq, cmp.Compare)
}
