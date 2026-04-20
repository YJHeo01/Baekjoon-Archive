import sys

input = sys.stdin.readline

n = int(input())

left = 0
right = 0
lecture = []
for _ in range(n):
    a,b = map(int,input().split())
    lecture.append((a,b))

lecture.sort()

answer = 1
while right < n:
    if lecture[left][1] > lecture[right][0]:
        answer = max(answer,(right-left)+1)
        right += 1
    else:
        if left == right:
            right += 1
        left += 1

print(answer)