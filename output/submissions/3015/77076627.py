import sys

input = sys.stdin.readline

n = int(input())

stack = []

answer = 0

for _ in range(n):
    right = int(input())
    mid = []
    while True:
        if stack == []:
            stack.append(right)
            break
        left = stack.pop()
        answer += 1
        if left > right:
            stack.append(left)
            stack += mid
            stack.append(right)
            break
        elif left == right:
            mid.append(left)

print(answer)