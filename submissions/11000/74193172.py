import sys

input = sys.stdin.readline

n = int(input())

lecture = []

for _ in range(n):
    lecture.append(list(map(int,input().split())))

lecture.sort()

left = 0
right = 0

answer = 0

while True:
    if right == n:
        break
    if lecture[left][1] > lecture[right][0]:
        right += 1
        answer = max(answer,right-left)
    else:
        left += 1

print(answer)