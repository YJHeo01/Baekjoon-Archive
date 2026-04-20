from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

parent = list(map(int,input().split()))

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    graph[parent[i]].append(i+2)
    
queue = deque([1])

depth = [-1] * (n+1)

cnt = [1] * (n+1)

depth[1] = 0

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        cnt[depth[nx]] += 1
        queue.append(nx)

if n == 2:
    print(1)
else:
    print(max(cnt[2:]))