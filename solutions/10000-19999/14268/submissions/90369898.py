import sys, math

sys.setrecursionlimit(2*10**5)

input = sys.stdin.readline

n,m = map(int,input().split())

tree = [[] for _ in range(n)]

parent = list(map(int,input().split()))

for i in range(1,n):
    tree[parent[i]-1].append(i)
    
ett = [[-1]*2 for _ in range(n)]

current_index = 0

def ddfs(x):
    global current_index
    ett[x][0] = current_index; current_index += 1
    for child in tree[x]:
        ddfs(child)
    ett[x][1] = current_index - 1

def dfs(graph,ett,x):
    for nx in graph[x]:
        ett[nx][0] = ett[x][1] + 1
        ett[nx][1] = ett[nx][0]
        ett[x][1] = dfs(graph,ett,nx)
    return ett[x][1]

ett[0][0], ett[0][1] = 0,0


ddfs(0)

seg_tree_size = 2 ** math.ceil(math.log2(n)+1)

seg_tree = [0] * seg_tree_size

lazy = [0] * seg_tree_size

def update_lazy(tree,lazy,node,start,end):
    #tree[node] += lazy[node] * (end-start+1)
    if start != end:
        lazy[node*2] += lazy[node]; lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def update(s,lazy,node,left,right,start,end,value):
    if lazy[node] != 0: 
        s[node] += lazy[node] * (end-start+1)
        update_lazy(s,lazy,node,start,end)
    if start > right or end < left: return
    if left <= start and end <= right:
        s[node] += value * (end-start+1)
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    mid = (start+end) // 2
    update(s,lazy,node*2,left,right,start,mid,value)
    update(s,lazy,node*2+1,left,right,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def qeury(s,lazy,node,left,right,start,end):
    if lazy[node] != 0:
        s[node] += (end-start+1) * lazy[node]
        update_lazy(s,lazy,node,start,end)
    if left <= start and end <= right:
        return s[node]
    if start > right or end < left: return 0
    if start == end:
        return s[node]
    mid = (start+end) // 2
    return qeury(s,lazy,node*2,left,right,start,mid) + qeury(s,lazy,node*2+1,left,right,mid+1,end)
    
sum_value = 0
   
for _ in range(m):
    command, *tmp = map(int,input().split())
    if command == 1:
        i,w = map(int,tmp)
        update(seg_tree,lazy,1,ett[i-1][0],ett[i-1][1],0,n-1,w)
        sum_value += w
    else:
        i = tmp[0]
        print(qeury(seg_tree,lazy,1,ett[i-1][0],ett[i-1][0],0,n-1))