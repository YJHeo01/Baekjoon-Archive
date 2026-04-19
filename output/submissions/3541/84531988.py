import sys

input = sys.stdin.readline

n,m = map(int,input().split())

answer = int(1e9)

for _ in range(m):
    u,d = map(int,input().split())
    left, right = 0, n
    while left <= right:
        mid = (left+right) // 2
        tmp = u * mid - d * (n-mid)
        if tmp > 0:
            answer = min(answer,tmp)
            right = mid - 1
        else:
            left = mid + 1

print(answer)