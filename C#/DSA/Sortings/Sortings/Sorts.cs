namespace Sortings
{
    public static class Sorts
    {
        public static T[] BubbleSort<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = enumerable.ToArray();
            int n = arr.Length;
            while (n > 1)
            {
                int border = 0;
                for (int i = 0; i < n - 1; i++)
                {
                    if (arr[i].CompareTo(arr[i + 1]) > 0)
                    {
                        (arr[i], arr[i + 1]) = (arr[i + 1], arr[i]);
                        border = i + 1;
                    }
                }
                n = border;
            }
            return arr;
        }
        
        public static T[] CocktailSort<T>(this IEnumerable<T> enumerable) where T: IComparable<T>
        {
            T[] arr = enumerable.ToArray();
            int left = 0;
            int right = arr.Length - 1;
            while (left < right)
            {
                int border = left; // or = 0;
                for (int i = left; i < right; i++)
                {
                    if (arr[i].CompareTo(arr[i + 1]) > 0)
                    {
                        (arr[i], arr[i + 1]) = (arr[i + 1], arr[i]);
                        border = i;
                    }
                }
                right = border;
                for (int i = right; i > left; i--)
                {
                    if (arr[i - 1].CompareTo(arr[i]) > 0)
                    {
                        (arr[i], arr[i - 1]) = (arr[i - 1], arr[i]);
                        border = i;
                    }
                }
                left = border;
            }
            return arr;
        }

        public static T[] InsertionSort<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = enumerable.ToArray();
            for (int i = 1; i < arr.Length; i++)
            {
                var item = arr[i];
                int j = i - 1;
                while (j >= 0 && arr[j].CompareTo(item) > 0)
                {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = item;
            }
            return arr;
        }
    }
}
