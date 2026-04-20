n = int(input())

answer = 0
for _ in range(n):
    word = list(input())
    stack = []
    for c in word:
        if stack == []:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        elif len(stack) >= 2:
            break
        else:
            stack.append(c)
    if stack == []:
        answer += 1

print(answer)