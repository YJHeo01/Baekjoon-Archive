import sys, math

sys.setrecursionlimit(2*10**5)

input = sys.stdin.readline

n,m = map(int,input().split())

tree = [[] for _ in range(n)]

parent = list(map(int,input().split()))

for i in range(1,n):
    tree[parent[i]-1].append(i)

ett = [[0]*2 for _ in range(n)]

def dfs(graph,ett,x):
    for nx in graph[x]:
        ett[nx][0] = ett[x][1] + 1
        ett[nx][1] = ett[nx][0]
        ett[x][1] = dfs(graph,ett,nx)
    return ett[x][1]

dfs(tree,ett,0)

seg_tree_size = 1 << math.ceil(math.log2(n)+1)

seg_tree = [0] * seg_tree_size

def update(s,node,target,start,end,value):
    mid = (start+end) // 2
    if start == end:
        s[node] += value
        return
    if target <= mid:
        update(s,node*2,target,start,mid,value)
    else:
        update(s,node*2+1,target,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def qeury(s,node,left,right,start,end):
    if left > end or start > right: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return qeury(s,node*2,left,right,start,mid)+ qeury(s,node*2+1,left,right,mid+1,end)

a = [0] * n
sum_value = 0

for _ in range(m):
    command, *tmp = map(int,input().split())
    if command == 1:
        i,w = map(int,tmp)
        update(seg_tree,1,ett[i-1][0],0,n-1,w)
    else:
        i = tmp[0]
        print(qeury(seg_tree,1,ett[i-1][0],ett[i-1][1],0,n-1))