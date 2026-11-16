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

func BubbleSortFunc[T any](seq iter.Seq[T], compare func(a, b T) int) []T {
	arr := slices.Collect(seq)
	bubble(arr, compare)
	return arr
}

func BubbleSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return BubbleSortFunc(seq, cmp.Compare[T])
}

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

func CocktailSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return CocktailSortFunc(seq, cmp.Compare[T])
}

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

func InsertionSort[T cmp.Ordered](seq iter.Seq[T]) []T {
	return InsertionSortFunc(seq, cmp.Compare[T])
}
