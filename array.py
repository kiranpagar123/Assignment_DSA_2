def count_pairs_with_sum(arr, target_sum):
    freq = {}
    count = 0
    for num in arr:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 7
count = count_pairs_with_sum(arr, target_sum)
print(count)  # Output: 3
