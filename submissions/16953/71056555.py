from collections import deque

a,b = map(int,input().split())

queue = deque([(a,1)])

INF = int(1e9)

answer = INF
while queue:
    value_cnt = queue.popleft()
    if value_cnt[0] == b:
        answer = value_cnt[1]
        break
    next_value = 10*value_cnt[0] + 1
    if next_value<= b:
        queue.append((next_value,value_cnt[1]+1))
    next_value = 2*value_cnt[0]
    if next_value <= b:
        queue.append((next_value,value_cnt[1]+1))

if answer == INF:
    answer = -1

print(answer)
