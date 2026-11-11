using Sortings;

namespace TestSortings
{
    public class TestSorts
    {
        static readonly int[] lens = [0, 1, 2, 100];
        static readonly IEnumerable<Func<IEnumerable<int>, int[]>> sortFuncs = [
            Sorts.BubbleSort,
            Sorts.CocktailSort,
            Sorts.InsertionSort,
            Sorts.DwarfSort,
            Sorts.SelectionSort,
            Sorts.QuickSortHoare,
            Sorts.QuickSortLomuto
        ];
        public static TheoryData<Func<IEnumerable<int>, int[]>, int> TestData = 
            ((Func<TheoryData<Func<IEnumerable<int>, int[]>, int>>)(() =>
            {
                var data = new TheoryData<Func<IEnumerable<int>, int[]>, int>();
                foreach (var func in sortFuncs)
                {
                    foreach (var len in lens)
                    {
                        data.Add(func, len);
                    }
                }
                return data;
            }))();

        static bool isSorted(int[] array)
        {
            for (int i = 0; i < array.Length - 1; i++)
            {
                if (array[i] > array[i + 1])
                {
                    return false;
                }
            }
            return true;
        }
        static int[] getUnsortedRand(int length, int start = -100, int end = 100)
        {
            int[] result = new int[length];
            Random rand = new();
            do
            {
                for ( int i = 0; i < result.Length; i++)
                {
                    result[i] = rand.Next(start, end + 1);
                }
                if (result.Length < 2) break;
            } while (isSorted(result));
            return result;
        }

        [Theory]
        [MemberData(nameof(TestData))]
        public void TestSort(Func<IEnumerable<int>, int[]> sortFunc, int length)
        {
            int[] arr = getUnsortedRand(length);
            int[] result = sortFunc(arr);
            Assert.True(isSorted(result));
        }
    }
}