import sys, math

sys.setrecursionlimit(2*10**5)

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n)]

parent = list(map(int,input().split()))

m = int(input())

for i in range(1,n):
    tree[parent[i]-1].append(i)

ett = [[0]*2 for _ in range(n)]

idx = 0

def dfs(graph,ett,x):
    for nx in graph[x]:
        ett[nx][0] = ett[x][1] + 1
        ett[nx][1] = ett[nx][0]
        ett[x][1] = dfs(graph,ett,nx)
    return ett[x][1]

dfs(tree,ett,0)

seg_tree_size = 1 << math.ceil(math.log2(n)+1)

seg_tree = [0] * seg_tree_size

lazy = [0] * seg_tree_size

def init(tree):
    for i in range(n):
        idx = seg_tree_size // 2 + i
        tree[idx] = 1
        idx //= 2
        while idx:
            tree[idx] = tree[idx * 2] + tree[idx*2+1]
            idx //= 2
    
init(seg_tree)

def update_lazy(tree,lazy,node,start,end):
    if lazy[node] == 1:
        tree[node] = end-start+1
    else:
        tree[node] = 0
    if start != end:
        lazy[node*2] = lazy[node]; lazy[node*2+1] = lazy[node]
        
    lazy[node] = 0

def update(s,lazy,node,left,right,start,end,value):
    if lazy[node] != 0: 
        update_lazy(s,lazy,node,start,end)
    if start > right or end < left: return
    if left <= start and end <= right:
        lazy[node] = value
        update_lazy(s,lazy,node,start,end)
        return
    mid = (start+end) // 2
    update(s,lazy,node*2,left,right,start,mid,value)
    update(s,lazy,node*2+1,left,right,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def query(s,lazy,node,left,right,start,end):
    if lazy[node] != 0:
        update_lazy(s,lazy,node,start,end)
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return query(s,lazy,node*2,left,right,start,mid) + query(s,lazy,node*2+1,left,right,mid+1,end)

for _ in range(m):
    command, i = map(int,input().split())
    if command != 3:
        update(seg_tree,lazy,1,ett[i-1][0]+1,ett[i-1][1],0,n-1,command)
    else:
        print(query(seg_tree,lazy,1,ett[i-1][0],ett[i-1][1],0,n-1)-1)