import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,time = map(int,input().split())
    graph[a].append((b,time))
    graph[b].append((a,time))

visited = [False] * (n+1)

INF = int(1e9)

def dfs(graph,visited,vx,road_list):
    visited[vx] = True
    if vx == n:
        road_list.sort(reverse=True)
        visited[vx] = False
        ret_value = sum(road_list)
        for i in range(k):
            ret_value -= road_list[i]
        return ret_value
    ret_value = INF
    for nx,time in graph[vx]:
        if visited[nx] == False:
            ret_value = min(ret_value,dfs(graph,visited,nx,road_list + [time]))
    visited[vx] = False
    return ret_value

answer = dfs(graph,visited,1,[])

print(answer)
