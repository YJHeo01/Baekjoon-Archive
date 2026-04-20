import sys

sys.setrecursionlimit(200000)

input = sys.stdin.readline

n,m = map(int,input().split())

leaf = set(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1] * n

depth[0] = 0

def set_depth(graph,depth,x):
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        set_depth(graph,depth,nx)
        
set_depth(graph,depth,0)    

#print(depth)

def set_target(graph,visited,depth,target,x):
    if visited[x]: return
    visited[x] = True
    for nx in graph[x]:
        if depth[nx] < depth[x]:
            target[nx].add(x)
            set_target(graph,visited,depth,target,nx)
            break

target = [set() for _ in range(n)]

visited = [False] * n

for i in leaf:
    set_target(graph,visited,depth,target,i)
    
answer = []

def solution(graph,target,x,answer):
    answer.append(x)
    if x in target: return
    for nx in graph[x]:
        if nx in target[x]:
            solution(graph,target,nx,answer)
            answer.append(x)
            
solution(graph,target,0,answer)

print(len(answer)-1)
print(*answer)