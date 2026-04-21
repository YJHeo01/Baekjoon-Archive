from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

adj_graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    adj_graph[a].append((b,c))
    adj_graph[b].append((a,c))

start,end = map(int,input().split())

weight = [0] * (n+1)

INF = int(1e9)

def solution(graph,weight,start):
    queue = deque([start])
    weight[start] = INF
    while queue:
        vx = queue.popleft()
        for nx,bridge_limit in graph[vx]:
            if min(weight[vx],bridge_limit) > weight[nx]:
                weight[nx] = min(weight[vx],bridge_limit)
                queue.append(nx)

solution(adj_graph,weight,start)

print(weight[end])