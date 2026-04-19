from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(n+1):
        graph[i].sort()
    
    s,e = map(int,input().split())
    s_e_distance = [-1] * (n+1)
    bfs(graph,s_e_distance,s)
    answer = s_e_distance[e]
    
    first_path = [False] * (n+1)
    dfs(graph,first_path,s_e_distance,s,e)
    first_path[s] = False
    
    e_s_visited = [-1] * (n+1)
    e_s_bfs(graph,first_path,e_s_visited,e)
    answer += e_s_visited[s]
    
    print(answer)

def bfs(graph,s_e_distance,start):
    queue = deque([start])
    s_e_distance[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if s_e_distance[nx] == -1:
                s_e_distance[nx] = s_e_distance[vx] + 1
                queue.append(nx)

def dfs(graph,first_path,s_e_distance,vx,target):
    if vx == target:
        return True
    for nx in graph[vx]:
        if s_e_distance[nx] == s_e_distance[vx] + 1:
            first_path[vx] = dfs(graph,first_path,s_e_distance,nx,target)
            if first_path[vx]: return True
    return False

def e_s_bfs(graph,first_path,e_s_distance,start):
    queue = deque([start])
    e_s_distance[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if first_path[nx] or e_s_distance[nx] != -1: continue
            e_s_distance[nx] = e_s_distance[vx] + 1
            queue.append(nx)

if __name__ == "__main__":
    main()