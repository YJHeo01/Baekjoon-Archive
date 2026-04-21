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
    visited = [-1] * (n+1)
    bfs(graph,visited,s)
    answer = visited[e]
    block = [False] * (n+1)
    dfs(graph,block,visited,s,e)
    block[s] = False
    e_s_visited = [-1] * (n+1)
    e_s_bfs(graph,block,e_s_visited,e)
    answer += e_s_visited[s]
    print(answer)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

def dfs(graph,block,visited,vx,target):
    if vx == target:
        return True
    for nx in graph[vx]:
        if visited[nx] == visited[vx] + 1:
            block[vx] = dfs(graph,block,visited,nx,target)
            if block[vx]: return True
    return False

def e_s_bfs(graph,block,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if block[nx] or visited[nx] != -1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)

if __name__ == "__main__":
    main()