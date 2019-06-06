def right_rotate_by_one(arr, length):
    temp = arr[length - 1]
    i = 0
    for i in range(length - 1, -1, -1):
        arr[i] = arr[i-1]
    arr[i] = temp


arr = [1,2,3,4,5,6,7]
length = len(arr)

right_rotate_by_one(arr, length)

print(*arr)
