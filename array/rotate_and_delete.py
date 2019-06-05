test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1: 
        print(arr[0])
    elif n%2 == 1:
        indices = n - 3
        indices = indices//4
        indices = indices + 3
        print(arr[indices-1])
    else:
        indices = n - 2
        indices = indices//4
        indices = indices + 2
        print(arr[indices-1])
