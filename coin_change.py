def coinChange(arr):
    arr.sort()
    currentChange = 0
    for number in arr:
        if currentChange + 1 < number:
            return currentChange + 1
        currentChange += number
    return currentChange + 1


arr = [1, 10, 3, 11, 6, 15];
print(coinChange(arr))