import sys, heapq

sys.setrecursionlimit(10**6+5)

input = sys.stdin.readline

INF = int(1e9)

n,m,start,end = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
	u,v,c = map(int,input().split())
	graph[u].append((v,c))
	graph[v].append((u,c))
distance = [INF] * (n+1)

q = []
heapq.heappush(q,(0,start))
distance[start] = 0
while q:
	dist, vx = heapq.heappop(q)
	if dist > distance[vx]: continue
	for nx, dd in graph[vx]:
		nd = dist + dd
		if nd >= distance[nx]: continue
		distance[nx] = nd
		heapq.heappush(q,(nd,nx))

possible = [False] * (n+1)

def dfs(graph,distance,possible,vx):
    
	possible[vx] = True
	if vx ==start: return
	for nx, dd in graph[vx]:
		if possible[nx]: continue
		if distance[nx] + dd == distance[vx]:
			dfs(graph,distance,possible,nx)

dfs(graph,distance,possible,end)

print(sum(possible))
for i in range(1,n+1):
	if possible[i]: print(i,end=" ")