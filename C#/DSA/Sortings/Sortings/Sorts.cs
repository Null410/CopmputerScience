namespace Sortings
{
    public static class Sorts
    {
        public static T[] BubbleSort<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = [.. enumerable];
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
            T[] arr = [.. enumerable];
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
            T[] arr = [.. enumerable];
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

        public static T[] DwarfSort<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = [.. enumerable];
            int i = 1;
            int j = i + 1;
            while (i < arr.Length)
            {
                if (i == 0 || arr[i].CompareTo(arr[i - 1]) >= 0)
                {
                    i = j;
                    ++j;
                }
                else
                {
                    (arr[i], arr[i - 1]) = (arr[i - 1], arr[i]);
                    --i;
                }
            }
            return arr;
        }

        public static T[] SelectionSort<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = [..enumerable];
            for (int i = 0; i < arr.Length; i++)
            {
                int min_idx = i;
                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[min_idx].CompareTo(arr[j]) > 0)
                    {
                        min_idx = j;
                    }
                }
                (arr[i], arr[min_idx]) = (arr[min_idx], arr[i]);
            }
            return arr;
        }

        private static void quickHoare<T>(T[] arr, int l, int r) where T : IComparable<T>
        {
            Func<T[], int, int, int> partition = (arr, l, r) =>
            {
                T pivot = arr[(r + l) / 2];
                int i = l;
                int j = r;
                while (i <= j)
                {
                    while (arr[i].CompareTo(pivot) < 0)
                    {
                        ++i;
                    }
                    while (arr[j].CompareTo(pivot) > 0)
                    {
                        --j;
                    }
                    if (i >= j)
                    {
                        break;
                    }
                    (arr[i], arr[j]) = (arr[j], arr[i]);
                    ++i;
                    --j;
                }
                return j;
            };

            if (l >= r) return;
            int p = partition(arr, l, r);
            quickHoare(arr, l, p);
            quickHoare(arr, p + 1, r);
        }

        /// <summary>
        /// Quick sort (Hoare scheme, by last).
        /// </summary>
        /// <typeparam name="T">IComparable</typeparam>
        /// <param name="enumerable">IEnumerable</param>
        /// <returns>A new sorted array T[]</returns>
        public static T[] QuickSortHoare<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = [.. enumerable];
            quickHoare(arr, 0, arr.Length - 1);
            return arr;
        }

        private static void quickLomuto<T>(T[] arr, int l, int r) where T : IComparable<T>
        {
            Func<T[], int, int, int> partition = (arr, l, r) =>
            {
                T pivot = arr[r];
                int p = l - 1;
                for (int i = l; i < r; i++)
                {
                    if (arr[i].CompareTo(pivot) <= 0)
                    {
                        ++p;
                        (arr[i], arr[p]) = (arr[p], arr[i]);
                    }
                }
                ++p;
                (arr[p], arr[r]) = (arr[r], arr[p]);
                return p;
            };
            if (l >= r) return;
            int p = partition(arr, l, r);
            quickLomuto(arr, l, p - 1);
            quickLomuto(arr, p + 1, r);
        }

        /// <summary>
        /// Quick sort (Lomuto scheme, by last).
        /// </summary>
        /// <typeparam name="T">IComparable</typeparam>
        /// <param name="enumerable">IEnumerable</param>
        /// <returns>A new sorted array T[]</returns>
        public static T[] QuickSortLomuto<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        {
            T[] arr = [.. enumerable];
            quickLomuto(arr, 0, arr.Length - 1);
            return arr;
        }
    }
}
