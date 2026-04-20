problem = list(input())
problem_length = len(problem)
stack = []
stack_top = -1
answer = 0 
for i in range(problem_length):
    if problem[i] == '(':
        if problem[i+1] != ')':
            answer += 1
        stack.append(i)
        stack_top += 1
    else:
        if stack[stack_top] == i-1:
            answer += stack_top
        stack_top -= 1
        stack.pop()

print(answer)