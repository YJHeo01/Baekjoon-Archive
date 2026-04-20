from collections import deque

n = int(input())

queue = deque(list(map(int,input().split())))

stack = []

answer = "Nice"

order = 1
while True:
    if order > n:
        break
    if stack != []:
        tmp = stack.pop()
        if tmp == order:
            order += 1
            continue
        stack.append(tmp)
    if queue != deque([]):
        tmp = queue.popleft()
        if order == tmp:
            order += 1
            continue
        if stack == []:
            stack.append(tmp)
        else:
            if tmp < stack[-1]:
                stack.append(tmp)
            else:
                answer = 'Sad'
                break
print(answer)