from collections import deque

def main():
    array = list(map(int,input().split()))
    a,b = map(int,input().split())
    print(bfs(array,[-1]*(n+1),a-1)[b-1])

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        nx = vx
        while True:
            nx += graph[vx]
            if nx >= n: break
            if visited[nx] != -1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
        nx = vx
        while True:
            nx -= graph[vx]
            if nx < 0: break
            if visited[nx] != -1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
    return visited

if __name__ == "__main__":
    n = int(input())
    main()