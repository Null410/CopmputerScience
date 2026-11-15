package sortings_test

import (
	"slices"
	"testing"

	sortings "github.com/null410/copmputerscience/go/DSA/Sortings"
)

func getUnsorted(length int) []int {
	result := make([]int, length)
	for i := range result {
		result[i] = len(result) - i - 1
	}
	return result
}

// A simple test (it will be changed later).
func TestUnsorted(t *testing.T) {
	arr := getUnsorted(10)
	sorted := sortings.BubbleSort(slices.Values(arr))
	if !slices.IsSorted(sorted) {
		t.Errorf("BubbleSort(%v) = %v", arr, sorted)
	}
}
