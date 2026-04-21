import sys, heapq

input = sys.stdin.readline

m,n,k = map(int,input().split())

start, dest = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    x,y,c = map(int,input().split())
    graph[x].append((y,c))
    
block = set()

for _ in range(k):
    block.add(tuple(map(int,input().split())))
    
    
INF = int(1e9)

distance = [dict() for _ in range(n)]

distance[start][0] = 0

q = []

heapq.heappush(q,(0,0,start))

while q:
    dist, last_x, x = heapq.heappop(q)
    if dist > distance[x][last_x]: continue
    for nx, dd in graph[x]:
        if (last_x,x,nx) in block: continue
        nd = dist + dd
        if x in distance[nx] and nd > distance[nx][x]: continue
        distance[nx][x] = nd
        heapq.heappush(q,(nd,x,nx))
        
answer = INF

for i in distance[dest]:
    answer = min(answer,distance[dest][i])

if answer >= INF: answer = -1

print(answer)