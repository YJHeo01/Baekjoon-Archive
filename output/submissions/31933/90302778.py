from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

min_list = []

for _ in range(m):
    u,v,l,r = map(int,input().split())
    min_list.append(l)
    graph[u].append((v,l,r))
    graph[v].append((u,l,r))

for i in range(1,n+1):
    graph[i].sort(key = lambda x:-x[2])
min_list.sort()

k = int(input())

fish = sorted(list(map(int,input().split())))

def dijkstra(graph,distance,min_size):
    queue = deque([1])
    distance[1] = INF
    while queue:
        vx = queue.popleft()
        for nx,l,r in graph[vx]:
            if min_size < l or min_size > r: continue
            nd = min(r,distance[vx])
            if nd > distance[nx]:
                distance[nx] = nd
                queue.append(nx)

answer = 0

idx = 0

left, right = 0,0

for i in min_list:
    distance = [0] * (n+1)
    dijkstra(graph,distance,i)
    if distance[n] < i: continue
    left = i
    right = max(right,distance[n])
    while True:
        if idx == k: break
        if fish[idx] < left: idx += 1
        elif fish[idx] <= right:
            idx += 1
            answer += 1
        else:
            break

print(answer)