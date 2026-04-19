from collections import deque
n = int(input())

array = list(map(int,input().split()))

child = [[] for _ in range(n)]

for i in range(1,n):
    child[array[i]].append(i)

indegree = [0] * n

for i in range(1,n):
    indegree[array[i]] += 1

start = []

for i in range(n):
    if indegree[i] == 0:
        start.append(i)

queue = deque(start)
time = [-1] * n

while queue:
    vx = queue.popleft()
    if child[vx] == []:
        time[vx] = 0
    else:
        child_cnt = 0
        chile_time = []
        for i in child[vx]:
            child_cnt += 1
            chile_time.append(time[i])
        chile_time.sort(reverse=True)
        for i in range(child_cnt):
            time[vx] = max(time[vx],chile_time[i]+i+1)
    if vx == 0: continue
    indegree[array[vx]] -= 1
    if indegree[array[vx]] == 0:
        queue.appendleft(array[vx])

print(time[0])