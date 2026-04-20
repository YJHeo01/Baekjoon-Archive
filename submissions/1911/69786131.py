import sys

input = sys.stdin.readline

n, l = map(int,input().split())

problem = []

for _ in range(n):
    a,b = map(int,input().split())
    problem.append((a,b))

left = 0
right = 0
answer = 0

problem.sort()

while 1:
    right += 1
    if (problem[right][0] - problem[left][1]) <= (l-2):
        right += 1
        if right >= n:
            answer += (((problem[right-1][1] - problem[left][0]-1) // l) + 1)
            break
    else:
        answer += (((problem[right-1][1] - problem[left][0]-1) // l) + 1)
        left = right

print(answer)