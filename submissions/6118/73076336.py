from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
INF = int(1e9)

distance_list = [INF] * (n+1)

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

bfs(graph,distance_list)
first_answer = 2
max_distance = 0
third_answer = 0
for idx in range(2,n+1):
    if distance_list[idx] > max_distance:
        max_distance = distance_list[idx]
        first_answer = idx
        third_answer = 1
    elif distance_list[idx] == max_distance:
        third_answer += 1
    else:
        continue
print(first_answer,distance_list[first_answer],third_answer)
