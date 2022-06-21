"""
if you find two different array
please make sure with two pointer

so take two pointer variable
loop through the two pointer by p1 < len(firstArray) and p2 < len(secondArray)
based on the condition increase the pointer
"""


def absDifference(arrayOne, arrayTwo):
    result = []
    if len(arrayOne) <= 0:
        return result
    p1 = 0
    p2 = 0
    minDiff = float("inf")
    arrayOne.sort()
    arrayTwo.sort()
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        absDiff = abs(arrayOne[p1] - (arrayTwo[p2]))
        if absDiff < minDiff:
            minDiff = absDiff
            result = [arrayOne[p1], arrayTwo[p2]]
        if arrayOne[p1] < arrayTwo[p2]:
            p1 += 1
        else:
            p2 += 1
    return result


print(absDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
