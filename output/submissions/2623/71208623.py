from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

def topology_sort():
    ret_value = []
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        value = queue.popleft()
        ret_value.append(value)
        for i in graph[value]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
            elif indegree[i] < 0:
                return [0]
    return ret_value
    


for _ in range(m):
    singers = list(map(int,input().split()))
    for i in range(1,singers[0]):
        graph[singers[i]].append(singers[i+1])
        indegree[singers[i+1]] += 1

answer = topology_sort()
if len(answer) != n:
    answer = [0]
    
for i in answer:
    print(i)