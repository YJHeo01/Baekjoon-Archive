from collections import deque

def main():
    graph = [[] for _ in range(n+1)]
    s,e = map(int,input().split())
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [-1] * (n+1)
    bfs(graph,visited,s)
    print(visited[e])

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    dx = [1,-1]
    while queue:
        vx = queue.popleft()
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx > n: continue
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()