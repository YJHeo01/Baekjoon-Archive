t = int(input())

def binary_search(array,right,i):
    right -= 1
    left = 0
    while left <= right:
        mid = (left+right) // 2
        if array[mid] > i:
            right = mid -1
        elif array[mid] < i:
            left = mid + 1
        else:
            return 1
    return 0

for _ in range(t):
    n = int(input())
    array1 = list(map(int,input().split()))
    array1.sort()
    m = int(input())
    array2 = list(map(int,input().split()))
    for i in array2:
        print(binary_search(array1,n,i))