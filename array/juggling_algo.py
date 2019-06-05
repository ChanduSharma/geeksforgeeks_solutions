# This is an implementation of the juggling algorithm
# used for swapping elements in blocks for rotation of
# array at a point.

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def left_rotate(arr,n,d):
    
    gcd_arr_depth = gcd(n,d)

    for i in range(gcd_arr_depth):

        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

arr = [1,2,3,4,5,6,7]
left_rotate(arr,len(arr),2)
print(*arr)
