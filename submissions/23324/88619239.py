from collections import deque
import sys

input = sys.stdin.readline

def main():

    n,m,k = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(k-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    start,end = map(int,input().split())
    
    for _ in range(k+1,m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n+1)
    
    bfs(graph,visited,start)
    
    if visited[end]:
        print(0)
        return
    
    start_connect_node_cnt = 0
    
    for i in range(n+1):
        if visited[i]: start_connect_node_cnt += 1
    
    print(start_connect_node_cnt*(n-start_connect_node_cnt))

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx]: continue
            visited[nx] = True
            queue.append(nx)

if __name__ == "__main__":
    main()