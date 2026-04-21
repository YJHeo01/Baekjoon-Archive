import sys

input = sys.stdin.readline

n = int(input())

tmp = [int(input()) for _ in range(n)]

arr = [0] * n

arr[0] = tmp[0]

for i in range(1,n):
    arr[i] = arr[i-1] + tmp[i]

length = sum(tmp)

answer = 0

def get_distance(a,b):
    if a > b: return arr[a] - arr[b]
    else: return length - arr[b] + arr[a]
    
for i in range(n):
    left = i + 1
    right = i + n - 1
    while left <= right:
        mid = (left+right) // 2
        idx = mid % n
        r_dist = get_distance(i,idx)
        l_dist = get_distance(idx,i)
        answer = max(answer,min(l_dist,r_dist))
        if l_dist < r_dist:
            right = mid - 1
        else:
            left = mid + 1
                      
print(answer)