import sys

input = sys.stdin.readline

n,d = map(int,input().split())

present = sorted([list(map(int,input().split())) for _ in range(n)])

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + present[i][1]

answer = 0

for i in range(n):
    target = i
    left, right = i,n-1
    while left <= right:
        mid = (left+right) // 2
        if present[mid][0] < present[i][0] + d:
            target = mid
            left = mid + 1
        else:
            right = mid - 1
    answer = max(answer,prefix_sum[target+1]-prefix_sum[i])

print(answer)