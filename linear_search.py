# linear search

def linear_search(arr, target):
    n = len(arr) + 1
    for i in range(n):
        if arr[i] == target:
            return i


arr = [11, 22, 33, 44, 55, 66, 77]
target = 55
linear_search(arr, target)