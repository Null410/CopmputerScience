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
    }
}