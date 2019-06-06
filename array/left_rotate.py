def left_rotate_by_one(arr, length):

    temp = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i+1]

    arr[length-1] = temp

# Example to test the function

arr = [1,2,3,4,5,6,7]
length = len(arr)

for i in range(2):
    left_rotate_by_one(arr,length)
print(*arr)
