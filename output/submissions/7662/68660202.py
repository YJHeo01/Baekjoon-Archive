from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    n = int(input())
    queue = deque([])
    for j in range(n):
        a,b=input().split()
        if a == 'I':
            queue.append(int(b))
        else:
            if queue != deque([]):
                sorted(queue)
                if b == '1':
                    queue.pop()
                else:
                    queue.popleft()
    sorted(queue)
    if queue != deque([]):
        print(queue[-1],queue[0])
    else:
        print("EMPTY")