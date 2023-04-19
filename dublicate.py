def find_duplicates(arr):
    freq = {}
    duplicates = []
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        if freq[num] > 1:
            duplicates.append(num)
    return duplicates
arr = [1, 2, 3, 4, 2, 5, 6, 1, 7, 7]
duplicates = find_duplicates(arr)
print(duplicates)  # Output: [1, 2, 7]
