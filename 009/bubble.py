def sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            return arr


# best O(n)
print sort([1, 2, 3, 4, 5, 6])
# average O(n^2)
print sort([4, 2, 3, 1, 6, 5])
# worst O(n^2)
print sort([6, 5, 4, 3, 2, 1])
