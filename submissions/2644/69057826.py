from collections import deque

def bfs(visited,start,end):
    i = 1
    queue = deque([start])
    visited[start] = i
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if visited[n] == 0:
                if n == end:
                    return visited[v]
                visited[n] = visited[v] + 1
                queue.append(n)
            


n = int(input())

a,b = map(int,input().split())

m = int(input())

graph = [[ ] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = bfs(visited,a,b)

if answer==None:
    answer=-1

print(answer)