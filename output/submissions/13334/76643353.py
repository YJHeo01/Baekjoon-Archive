import sys

input = sys.stdin.readline

n = int(input())

line = []

for _ in range(n):
    left, right = map(int,input().split())
    if left > right:
        left, right = right, left
    line.append([left,right])

line.sort()

d = int(input())

answer = 0

left = 0
right = 0
while True:
    if line[left][0] + d >= line[right][1]:
        right += 1
        answer = max(answer,right-left)
    else:
        left += 1
        if left > right:
            right = left
    if right == n:
        break
print(answer)