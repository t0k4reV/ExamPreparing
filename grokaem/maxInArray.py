def maxArr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maxArr(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(maxArr([4, 5, 2, 3]))
