def reverse_list(arr, start, end):

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def left_rotate(arr, length, d):

    reverse_list(arr, 0, d - 1)
    reverse_list(arr, d, length - 1)
    reverse_list(arr, 0, length - 1)

arr = [1,2,3,4,5,6,7,8]
length = len(arr)
d = 2

left_rotate(arr, length, d)
print(*arr)
