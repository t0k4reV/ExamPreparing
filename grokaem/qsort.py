from typing import List


def qsortup(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return qsortup(less) + [pivot] + qsortup(greater)


def qsortdown(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return qsortdown(greater) + [pivot] + qsortdown(less)


print(sorted(list(range(10000, 0, -1))))
