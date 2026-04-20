from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

deq = deque([])

for _ in range(n):
    command = list(map(int,input().split()))
    
    if command[0] == 1:
        deq.appendleft(command[1])
    elif command[0] == 2:
        deq.append(command[1])
    elif command[0] == 3:
        if deq != deque([]):
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 4:
        if deq != deque([]):
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 5:
        print(len(deq))
    elif command[0] == 6:
        if deq == deque([]):
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if deq == deque([]):
            print(-1)
        else:
            print(deq[0])
    else:
        if deq == deque([]):
            print(-1)
        else:
            print(deq[-1])