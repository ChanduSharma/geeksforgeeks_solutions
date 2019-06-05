def rotate_right_by_one(arr, length):
    temp = arr[length - 1]
    print(arr)
    for i in range(length-1,-1,-1):
        arr[i] = arr[i-1]
        print(arr)
    arr[0] = temp
    
    
test_cases = int(input())

for i in range(test_cases):
    length = int(input())
    arr = list(map(int, input().split()))
    rotate_right_by_one(arr,length)
    print(arr)
    print(arr[0])
