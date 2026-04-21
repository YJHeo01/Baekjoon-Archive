from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    parent = list(range(n+1))
    graph = [[] for _ in range(n+1)]
    answer = 0
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a)
        if union_parent(parent,a,b) == False:
            answer += 1
    visited = [False] * (n+1)
    for i in range(1,n+1):
        if visited[i] == False:
            bfs(graph,visited,i)
            answer += 1
    answer -= 1
    print(answer)

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b: return False
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)

if __name__ == "__main__":
    main()