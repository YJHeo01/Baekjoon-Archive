import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
INF = int(1e9)

distance = [INF] * (n+1)

input()

house = sorted(list(map(int,input().split())))

store = list(map(int,input().split()))

q = []

for i in store:
    distance[i] = 0
    heapq.heappush(q,(0,i))
    
while q:
    dist, x = heapq.heappop(q)
    if dist > distance[x]: continue
    for nx, dd in graph[x]:
        nd = dist + dd
        if distance[nx] > nd:
            distance[nx] = nd
            heapq.heappush(q,(nd,nx))

answer = house[0]

for i in house:
    if distance[answer] > distance[i]:
        answer = i

print(answer)