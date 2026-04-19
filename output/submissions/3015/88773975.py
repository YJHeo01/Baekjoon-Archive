import sys

input = sys.stdin.readline

n = int(input())

stack = []

answer = 0

for _ in range(n):
    right = int(input())
    same = False
    while stack:
        left,cnt = stack.pop()
        answer += cnt
        if left > right:
            stack.append((left,cnt)); break
        if left == right:
            stack.append((left,cnt+1))
            answer += cnt
            same = True
            break
    if not same:
        stack.append((right,1))

print(answer)