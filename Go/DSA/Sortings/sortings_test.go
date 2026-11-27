package sortings_test

import (
	"fmt"
	"iter"
	"math/rand"
	"slices"
	"strconv"
	"strings"
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
		{"InsertionSort", sortings.InsertionSort[int]},
		{"DwarfSort", sortings.DwarfSort[int]},
		{"SelectionSort", sortings.SelectionSort[int]},
		{"QuickSortLomuto", sortings.QuickSortLomuto[int]},
		{"QuickSortHoare", sortings.QuickSortHoare[int]},
		{"MergeSort", sortings.MergeSort[int]},
		{"CombSort", sortings.CombSort[int]},
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

func getUnsorted(length int) []int {
	result := make([]int, length)
	min := -100
	max := 100
	rangeRand := max - min + 1
	for {
		for i := range result {
			result[i] = min + rand.Intn(rangeRand)
		}
		if len(result) < 2 || !slices.IsSorted(result) {
			return result
		}
	}
}

func formatSlice(arr []int) string {
	var sb strings.Builder
	sb.WriteByte('[')
	for i := 1; i < len(arr); i++ {
		item := strconv.Itoa(arr[i])
		if arr[i] < arr[i-1] {
			sb.WriteByte('(')
			sb.WriteString(item)
			sb.WriteByte(')')
		} else {
			sb.WriteString(item)
		}
		if i != len(arr)-1 {
			sb.WriteByte(' ')
		}
	}
	sb.WriteByte(']')
	return sb.String()
}

func TestUnsorted(t *testing.T) {
	cases := getTestData()
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			arr := getUnsorted(c.len)
			sorted := c.function(slices.Values(arr))
			if !slices.IsSorted(sorted) {
				t.Errorf("%s(%v) = %s", c.name, arr, formatSlice(sorted))
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
