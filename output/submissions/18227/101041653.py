import sys, math
from collections import deque

input = sys.stdin.readline

n,c = map(int,input().split())

graph = [[] for _ in range(n)]

depth = [-1] * n

for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

c -= 1

queue = deque([c])

depth[c] = 1

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if depth[nx] != -1: continue
        depth[nx] = depth[x] + 1
        queue.append(nx)

ett = [[0]*2 for _ in range(n)]

def dfs(graph,ett,x):
    for nx in graph[x]:
        if depth[nx] < depth[x]: continue
        ett[nx][0] = ett[x][1] + 1
        ett[nx][1] = ett[nx][0]
        ett[x][1] = dfs(graph,ett,nx)
    return ett[x][1]

dfs(graph,ett,c)

seg_size = 1 << math.ceil(math.log2(n)+1)

s = [0] * seg_size

lazy = [0] * seg_size

def update_lazy(s,lazy,node,start,end):
    s[node] += lazy[node] * (end - start + 1)
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0
    
def update(s,lazy,node,left,right,start,end,value):
    if lazy[node] != 0:
        update_lazy(s,lazy,node,start,end)
    if start > right or end < left: return
    l_node, r_node = node*2, node*2+1
    if left <= start and end <= right:
        s[node] += value * (end - start + 1)
        if start != end:
            lazy[l_node] += value
            lazy[r_node] += value
        return
    mid = (start+end) // 2
    update(s,lazy,l_node,left,right,start,mid,value)
    update(s,lazy,r_node,left,right,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]
    
def query(s,lazy,node,left,right,start,end):
    if lazy[node] != 0:
        update_lazy(s,lazy,node,start,end)
    if end < left or right < start: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return query(s,lazy,2*node,left,right,start,mid) + query(s,lazy,2*node+1,left,right,mid+1,end)

q = int(input())

for _ in range(q):
    command, a = map(int,input().split())
    a -= 1
    if command == 1:
        update(s,lazy,1,ett[a][0],ett[a][0],0,n-1,1)
    else:
        print(depth[a]*query(s,lazy,1,ett[a][0],ett[a][1],0,n-1))