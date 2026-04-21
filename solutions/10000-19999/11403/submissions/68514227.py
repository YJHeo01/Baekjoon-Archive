from collections import deque

def bfs(graph,visited,start):
    queue = deque(graph[start])
    while queue:
        v = queue.popleft()
        visited[start][v] = 1
        for i in graph[v]:
            if visited[start][i] == 0:
                visited[start][i] = 1
                queue.append(i)

n = int(input())
visited = [[0]*n for _ in range(n)]
graph = [ [] for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i].append(j)

for v in range(n):
    bfs(graph,visited,v)

for i in range(n):
    for j in range(n):
        print(visited[i][j],end = ' ')
    print()
