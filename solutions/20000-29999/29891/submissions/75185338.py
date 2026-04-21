import sys

input = sys.stdin.readline

n,k = map(int,input().split())
checkpoint = [0]

answer = 0

for _ in range(n):
    checkpoint.append(int(input()))

checkpoint.sort()

zero_idx = 0

left, right = 0,n
while left <= right:
    mid = (left+right) // 2
    if checkpoint[mid] > 0:
        right = mid - 1
    elif checkpoint[mid] < 0:
        left = mid + 1
    else:
        zero_idx = mid
        break

for i in range(0,zero_idx,k):
    answer -= checkpoint[i]

for i in range(n,zero_idx,-k):
    answer += checkpoint[i]

answer *= 2

print(answer)