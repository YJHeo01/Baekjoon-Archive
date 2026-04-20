s = input()

answer = ''

stack = []

num = 0

prior = 0

for c in s:
    if c == '(':
        num += 1
    elif c == ')':
        num -= 1
        if num == 0:
            while stack:
                answer += stack.pop()
    elif c == '*' or c == '/':
        stack.append(c)
    elif c == '+' or c == '-':
        if num == 0:
            while stack:
                answer += stack.pop()
        stack.append(c)
    else:
        answer += c
        
while stack:
    answer += stack.pop()

print(answer)