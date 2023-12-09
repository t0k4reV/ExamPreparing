def countElements(arr):
    if arr == []:
        return 0
    return 1 + countElements(arr[1:])


print(countElements([1, 3, 4, 4, 6]))
