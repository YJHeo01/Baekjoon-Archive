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
            prior = 0
            while stack:
                answer += stack.pop()
    elif c == '*' or c == '/':
        prior = 1
        stack.append(c)
    elif c == '+' or c == '-':
        if num == 0 and prior == 1:
            while stack:
                answer += stack.pop()
        prior = 0
        stack.append(c)
    else:
        answer += c
        
while stack:
    answer += stack.pop()

print(answer)