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
        if left > right:
            answer += 1
            stack.append((left,cnt)); break
        if left == right:
            answer += cnt
            if stack != []: answer += 1
            stack.append((left,cnt+1))
            same = True
            break
        answer += cnt
    if not same:
        stack.append((right,1))

print(answer)