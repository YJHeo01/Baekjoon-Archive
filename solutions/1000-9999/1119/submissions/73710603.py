from collections import deque

n = int(input())
adj_graph = [[]for _ in range(n)]
road_cnt = 0
for i in range(n):
    tmp = list(input())
    for j in range(i+1,n):
        if tmp[j] == 'Y':
            adj_graph[i].append(j)
            adj_graph[j].append(i)
            road_cnt += 1

def bfs(graph,visited,start):
    if graph[start] == []:
        return -1
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)
    return 0

visited = [False] * n

answer = -1

if road_cnt >= n-1:
    for i in range(n):
        if visited[i] == False:
            answer += 1
            if bfs(adj_graph,visited,i) == -1:
                answer = -1
                break

if n == 1:
    answer = 0

print(answer)