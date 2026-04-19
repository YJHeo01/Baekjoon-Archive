from collections import deque
import sys

input = sys.stdin.readline

n,start,end = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,length = map(int,input().split())
    graph[a].append((b,length))
    graph[b].append((a,length))


INF = int(1e9)

distance = [INF] * (n+1)

max_length = [0] * (n+1)

def solution(graph,distance,max_length,start):
    queue = deque([start])
    distance[start] = 0
    max_length[start] = 0
    while queue:
        vx = queue.popleft()
        for nx, length in graph[vx]:
            if distance[nx] > distance[vx] + length:
                distance[nx] = distance[vx] + length
                max_length[nx] = max(max_length[vx],length)
                queue.append(nx)
    
solution(graph,distance,max_length,start)

answer = distance[end] - max_length[end]

print(answer)