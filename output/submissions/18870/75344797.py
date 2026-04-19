n = int(input())

num_list = list(map(int,input().split()))

tmp = []

for i in range(n):
    tmp.append(num_list[i])

tmp.sort()

idx = [tmp[0]]
max_idx = 0

for i in range(1,n):
    if tmp[i] != tmp[i-1]:
        idx.append(tmp[i])
        max_idx += 1

def binary_search(idx,value):
    left, right = 0, max_idx
    while left <= right:
        mid = (left+right) // 2
        if idx[mid] < value:
            left = mid + 1
        elif idx[mid] > value:
            right = mid - 1
        else:
            return mid
        
for num in num_list:
    print(binary_search(idx,num),end=" ")