def move_negatives(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
arr = [-1, 2, -3, 4, 5, -6, -7, 8, 9]
modified_arr = move_negatives(arr)
print(modified_arr)
