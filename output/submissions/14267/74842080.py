from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

array = list(map(int,input().split()))

for i in range(1,n):
    graph[array[i]].append(i+1)

compliment = [0] * (n+1)

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    ret_value = [start]
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)
                ret_value.append(nx)
    return ret_value

for _ in range(m):
    i,w = map(int,input().split())
    visited = [False] * (n+1)
    good_member_list = bfs(graph,visited,i)
    for good_member in good_member_list:
        compliment[good_member] += w
for i in range(1,n+1):
    print(compliment[i],end=" ")