from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

line_up = list(map(int,input().split()))

INF = int(1e9)

depth = [INF] * (n+1)

visited_order = [0] * (n+1)

for i in range(n):
    visited_order[line_up[i]] = i

parent = [0] * (n+1)

def solution(graph,depth,parent):
    queue = deque([1])
    depth[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if depth[nx] > depth[vx] + 1:
                depth[nx] = depth[vx]+ 1
                parent[nx] = vx
                queue.append(nx)

answer = 1

solution(graph,depth,parent)

for i in range(1,n):
    if depth[line_up[i]] < depth[line_up[i-1]]:
        answer = 0
        break
    if depth[line_up[i]] == depth[line_up[i-1]] and visited_order[parent[line_up[i]]] < visited_order[parent[line_up[i-1]]]:
        answer = 0
        break
print(answer)