s = list(input())

stack = []

grade = 0

last_c = 'c'

for c in s:
    if c == '(':
        grade += 2
    elif c == ')':
        while stack:
            a,b = stack.pop()
            if b < grade:
                stack.append((a,b))
                break
            print(a,end="")
        grade -= 2
    elif c == '+' or c == '-':
        while stack:
            a, b = stack.pop()
            if b < grade:
                stack.append((a, b))
                break
            print(a, end="")
        stack.append((c,grade))
    elif c == '*' or c == '/':
        while stack:
            a, b = stack.pop()
            if b < grade + 1:
                stack.append((a, b))
                break
            print(a, end="")
        stack.append((c,grade+1))
    else:
        print(c,end="")

while stack:
    a,b = stack.pop()
    print(a,end="")