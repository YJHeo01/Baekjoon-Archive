def binary_search(start,i,array,end):
    while start <= end:
        mid = ((start+end)//2)
        if array[mid] == i:
            return 1
        elif array[mid] > i:
            end = mid - 1
        elif array[mid] < i:
            start = mid + 1
    return 0
    

n = int(input())

array = list(map(int,input().split()))

m = int(input())

array_ = list(map(int,input().split()))

array.sort()

for i in array_:
    print(binary_search(0,i,array,n-1))