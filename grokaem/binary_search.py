def binary_search(my_list, n):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == n:
            return mid
        if guess > n:
            high = mid - 1
        if guess < n:
            low = mid + 1
    return -1


print(binary_search([1, 3, 5, 6], 3))
