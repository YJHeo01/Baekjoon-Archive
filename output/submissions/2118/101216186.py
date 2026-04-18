import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

prefix_sum = [0] * n

prefix_sum[0] = arr[0]

for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

length = sum(arr)

answer = 0

def get_distance(a,b):
    if a > b: return prefix_sum[a] - prefix_sum[b]
    else: return length - prefix_sum[b] + prefix_sum[a]
    
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
            left = mid + 1
        else:
            right = mid - 1
                      
print(answer)