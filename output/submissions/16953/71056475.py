from collections import deque

a,b = map(int,input().split())

queue = deque([(a,1)])

INF = int(1e9)

answer = INF
while queue:
    value = queue.popleft()
    if value[0] == b:
        answer = min(answer,value[1])
    next_value = 10*value[0] + 1
    if next_value<= b:
        queue.append((next_value,value[1]+1))
    next_value = 2*value[0]
    if next_value <= b:
        queue.append((next_value,value[1]+1))

if answer == INF:
    answer = -1

print(answer)