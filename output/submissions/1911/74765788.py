import sys

input = sys.stdin.readline

n,l = map(int,input().split())

hole = []

for _ in range(n):
    hole.append(list(map(int,input().split())))

hole.sort()

answer = 0
last_right = -1

for i in range(n):
    left, right = hole[i]
    left = max(left,last_right)
    if (right-left) % l == 0:
        last_right = right
        answer += (right-left) // l
    else:
        tmp = (right-left) // l
        answer += tmp
        answer += 1
        last_right = left + (tmp+1) * l

print(answer)