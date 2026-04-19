from collections import deque
q = deque(list(range(1,int(input())+1)))
while 1:
    if len(q)==0:break
    print(q.popleft(),end=" ")
    if len(q)==0:break
    q.append(q.popleft())