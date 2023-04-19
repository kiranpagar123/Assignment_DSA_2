def find_kth_largest_smallest_sorting(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]
arr = [3, 7, 2, 9, 4, 1, 8, 5, 6]
k = 3
kth_smallest, kth_largest = find_kth_largest_smallest_sorting(arr, k)
print(f"The {k}th smallest number is {kth_smallest}")
print(f"The {k}th largest number is {kth_largest}")
