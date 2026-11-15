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
