from collections import deque

problem = deque(list(input()))

stack = []
stack_top = -1
answer = 0
idx = 0 
while problem != deque([]):
    value = problem.popleft()
    if value == '(':
        if problem[0] != ')':
            answer += 1
        stack.append(idx)
        stack_top += 1
    else:
        if stack[stack_top] == idx-1:
            answer += stack_top
        stack_top -= 1
        stack.pop()
    idx += 1

print(answer)
