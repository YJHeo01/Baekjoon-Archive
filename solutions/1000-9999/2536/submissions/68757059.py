from collections import deque
import sys

INF = int(1e9)
m,n = map(int,input().split())
visited = [[INF]*(m+1) for _ in range(n+1)]

def bfs(graph,visited,start,move):
    queue = deque([start])
    visited[start[1]][start[0]] = 0
    while queue:
        vx, vy = queue.popleft()
        b = graph[vy][vx]
        for i in b:
            for j in move[i]:
                if visited[j[1]][j[0]] > visited[vy][vx] + 1:
                    visited[j[1]][j[0]] = visited[vy][vx] + 1
                    queue.append((j[0],j[1]))
bus_list = [[[] for _ in range(m+1)]for _ in range(n+1)]
k = int(input())
bus = [[]for _ in range(k+1)]
for i in range(k):
    b,x1,y1,x2,y2 = map(int,input().split())
    if x1 == x2:
        if y1 > y2 :
            y1, y2 = y2, y1
        for i in range(y1,y2+1):
            bus_list[i][x1].append(b)
            bus[b].append((x1,i))
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        for i in range(x1,x2+1):
            bus_list[y1][i].append(b)
            bus[b].append((i,y1))

x1,y1,x2,y2 = map(int,input().split())

bfs(bus_list,visited,(x1,y1),bus)
print(visited[y2][x2])