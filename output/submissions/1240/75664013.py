from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

distance = [[INF]*(n+1) for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def solution(graph,distance,start):
    queue = deque([start])
    distance[start][start] = 0
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if distance[start][nx] > distance[start][vx] + length:
                distance[start][nx] = distance[start][vx] + length
                queue.append(nx)

for i in range(1,n+1):
    solution(graph,distance,i)

for _ in range(m):
    a,b = map(int,input().split())
    print(distance[a][b])