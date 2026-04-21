from collections import deque
import sys

input = sys.stdin.readline

v,e = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(v+1)]
adj_matrix = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,w = map(int,input().split())
    if adj_matrix[a][b] == INF:
        graph[a].append(b)
        graph[b].append(a)
        adj_matrix[a][b] = w
        adj_matrix[b][a] = w
    else:
        adj_matrix[a][b] = min(adj_matrix[a][b],w)
        adj_matrix[b][a] = min(adj_matrix[b][a],w)

house = [True] * (v+1)

m,x = map(int,input().split())

mcdonald = list(map(int,input().split()))

for i in mcdonald:
    house[i] = False

s,y = map(int,input().split())

starbucks = list(map(int,input().split()))

for i in starbucks:
    house[i] = False

mcdonald_distance = [x+1] * (v+1)
starbucks_distance = [y+1] * (v+1)

def bfs(graph,adj_matrix,distance,start):
    queue = deque(start)
    for i in start:
        distance[i] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if distance[nx] > distance[vx] + adj_matrix[vx][nx]:
                distance[nx] = distance[vx] + adj_matrix[vx][nx]
                queue.append(nx)

bfs(graph,adj_matrix,mcdonald_distance,mcdonald)
bfs(graph,adj_matrix,starbucks_distance,starbucks)

answer = INF

for i in range(1,v+1):
    if mcdonald_distance[i] > x or starbucks_distance[i] > y:
        continue
    answer = min(answer,mcdonald_distance[i]+starbucks_distance[i])

if answer >= INF:
    answer = -1

print(answer)