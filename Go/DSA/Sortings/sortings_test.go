package sortings_test

import (
	"fmt"
	"iter"
	"slices"
	"testing"

	sortings "github.com/null410/copmputerscience/go/DSA/Sortings"
)

type sortFunc struct {
	name     string
	function func(iter.Seq[int]) []int
}

func getSorts() []sortFunc {
	return []sortFunc{
		{"BubbleSort", sortings.BubbleSort[int]},
		{"CocktailSort", sortings.CocktailSort[int]},
	}
}

func getLens() []int {
	return []int{100, 2, 1, 0}
}

type testData struct {
	sortFunc
	len int
}

func getTestData() []testData {
	sorts := getSorts()
	lens := getLens()
	data := make([]testData, 0, len(sorts)*len(lens))
	for _, sort := range sorts {
		for _, len := range lens {
			data = append(data, testData{
				name:     fmt.Sprintf("%s_%v", sort.name, len),
				function: sort.function,
				len:      len,
			})
		}
	}
	return data
}

// Will be modified to test a random unsorted sequence.
func getUnsorted(length int) []int {
	result := make([]int, length)
	for i := range result {
		result[i] = len(result) - i - 1
	}
	return result
}

func TestUnsorted(t *testing.T) {
	cases := getTestData()
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			arr := getUnsorted(c.len)
			sorted := c.function(slices.Values(arr))
			if !slices.IsSorted(sorted) {
				t.Errorf("%s(%v) = %v", c.name, arr, sorted)
			}
		})
	}
}

func getSorted(length int) []int {
	result := make([]int, length)
	for i := range result {
		result[i] = i
	}
	return result
}

func TestSorted(t *testing.T) {
	cases := getSorts()
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			n := 100
			arr := getSorted(n)
			sorted := c.function(slices.Values(arr))
			if !slices.IsSorted(sorted) {
				t.Errorf("%s = %v", c.name, sorted)
			}
		})
	}
}
