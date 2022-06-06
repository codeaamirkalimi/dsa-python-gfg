def binary_search(nums, low, high, find_num):
    mid = (high - low) / 2
    for i in range(len(nums)):
        mid = (low + high)/2

        if find_num == arr[int(mid)]:
            return mid

        if find_num > arr[int(mid)]:
            return binary_search(arr,
                                (mid + 1), high, find_num)

        if find_num < arr[int(mid)]:
            return binary_search(arr,low, (mid-1), find_num)

    return 0


arr = [5, 6, 7, 8, 9, 10]
print('Result', binary_search(arr, 0, len(arr), 10))
