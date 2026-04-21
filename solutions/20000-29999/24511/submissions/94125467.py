from collections import deque

n = int(input())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

m = int(input())

c = list(map(int,input().split()))

queue_stack = []

for i in range(n):
    queue_stack.append(deque([b[i]]))

for c_i in c:
    value = c_i
    for i in range(n):
        queue_stack[i].append(value)
        if a[i] == 1:
            value = queue_stack[i].pop()
        else:
            value = queue_stack[i].popleft()
    print(value,end=" ")