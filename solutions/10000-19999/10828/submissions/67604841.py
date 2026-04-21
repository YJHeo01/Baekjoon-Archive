n = int(input())
stack = []
for i in range(n):
    cmd = input()
    if cmd[0] == 't':
      if stack == []:print(-1)
      else: print(stack[-1])
    elif cmd[0] == 'e':
      if stack == []:print(1)
      else: print(0)
    elif cmd[0] == 's': print(len(stack))
    elif cmd[0:2] == 'pu':stack.append(int(cmd[5:]))
    else:
       if stack == [] : print(-1)
       else : print(stack.pop())