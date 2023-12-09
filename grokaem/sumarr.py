def summArray(arr):
    total = 0
    for i in arr:
        total += i
    return total


def recursionSumm(arr):
    if arr == []:
        return 0
    return arr[0] + recursionSumm(arr[1:])


print(summArray([1, 2, 3, 4, 5, 6]))
print(recursionSumm([1, 2, 3, 4, 5, 6]))
