n = int(input())

answer = 0

stack = []

for _ in range(n):
    right = int(input())
    if stack == []:
        stack.append(right)
        continue
    while stack != []:
        left = stack.pop()
        answer += 1
        if left > right or stack == []:
            stack.append(left)
            break
    stack.append(right)
print(answer)