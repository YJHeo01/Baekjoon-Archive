from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [-1] * (n+1)

queue = deque([1])

sparse_table = [[0]*21 for _ in range(n+1)]

depth[1] = 0

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        sparse_table[nx][0] = x
        queue.append(nx)
        
for j in range(1,21):
    for i in range(1,n+1):
        sparse_table[i][j] = sparse_table[sparse_table[i][j-1]][j-1]
        
def get_lca(a,b):
    if depth[a] > depth[b]: a,b = b,a
    for i in range(20,-1,-1):
        if depth[b] - (1<<i) >= depth[a]:
            b = sparse_table[b][i]
    if a == b: return a
    for i in range(20,-1,-1):
        if sparse_table[a][i] != sparse_table[b][i]:
            a = sparse_table[a][i]
            b = sparse_table[b][i]
    return sparse_table[a][0]

answer = 0

m = int(input())

cur_city = 1

for _ in range(m):
    next_city = int(input())
    lca = get_lca(cur_city,next_city)
    answer += (depth[cur_city] + depth[next_city] - depth[lca])
    cur_city = next_city

print(answer)