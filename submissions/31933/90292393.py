import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,l,r = map(int,input().split())
    graph[u].append((v,l,r))
    graph[v].append((u,l,r))
    
k = int(input())

fish = sorted(list(map(int,input().split())))

tmp = []

def dfs(graph,visited,vx,min_size,max_size):
    if vx == n:
        global tmp
        tmp.append((min_size,max_size))
        return
    for nx,l,r in graph[vx]:
        if visited[nx]: continue
        n_min = max(l,min_size)
        n_max = min(r,max_size)
        if n_min > n_max: continue
        visited[nx] = True
        dfs(graph,visited,nx,n_min,n_max)
        visited[nx] = False
        
visited = [False] * (n+1)
visited[1] = True

dfs(graph,visited,1,0,int(1e9))

tmp.sort()

idx = 0

answer = 0

left, right = 0,0

for a,b in tmp:
    left = a
    right = max(right,b)
    while True:
        if idx == k: break
        if fish[idx] < left: idx += 1
        elif fish[idx] <= right:
            idx += 1
            answer += 1
        else:
            break

print(answer)
        