import sys

input = sys.stdin.readline

n = int(input())

answer = 0

stack = []

for _ in range(n):
    right = int(input())
    next_push = []
    if stack == []:
        stack.append(right)
        continue
    while stack != []:
        left = stack.pop()
        answer += 1
        if left > right:
            stack.append(left)
            break
        elif left == right:
            next_push.append(left)
    next_push.reverse()
    stack += next_push
    stack.append(right)
print(answer)