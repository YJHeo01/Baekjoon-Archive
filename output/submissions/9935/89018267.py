s = list(input())
target = list(input())
target_length = len(target)
stack = []

for c in s:
    stack.append(c)
    while stack:
        tmp = []
        bomb = True
        for i in range(target_length):
            if stack == []:
                bomb = False
                break
            head = stack.pop()
            tmp.append(head)
            if target[target_length-1-i] != head:
                bomb = False
                break
        if bomb == False:
            while tmp:
                stack.append(tmp.pop())
            break
if stack == []:
    print("FRULA")
    exit(0)

for c in stack:
    print(c,end="")