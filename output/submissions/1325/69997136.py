import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int,input().split())

def bfs(graph,start):
    ret_v = 0
    visited = [0] * (n+1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == 0:
                visited[nx] = 1
                ret_v += 1
                queue.append(nx)

    return ret_v

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

answer = []
max_v = 0
for i in range(1,n+1):
    tmp = bfs(graph,i)
    if tmp > max_v:
        answer = [i]
        max_v = tmp
    elif tmp == max_v:
        answer.append(i)
    else:
        continue

for i in answer:
    print(i,end=" ")