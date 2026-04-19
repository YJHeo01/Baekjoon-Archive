import sys, math

sys.setrecursionlimit(2*10**5)

n,m = map(int,input().split())

boss = list(map(int,input().split()))

tree = [[] for _ in range(n)]

for i in range(1,n):
    tree[boss[i]-1].append(i)
    
ett = [[0]*2 for _ in range(n)]

def dfs(tree,ett,x):
    for nx in tree[x]:
        ett[nx][0] = ett[x][1] + 1
        ett[nx][1] = ett[nx][0]
        ett[x][1] = dfs(tree,ett,nx)
    return ett[x][1]

dfs(tree,ett,0)

tree_size = 2 ** math.ceil(math.log2(n)+1)


def update(s,lazy,node,left,right,start,end,value):
    if lazy[node] != 0: update_lazy(s,lazy,node,start,end)
    if left > end or start > right: return
    if left <= start and end <= right:
        s[node] += value
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    mid = (start+end) // 2
    update(s,lazy,node*2,left,right,start,mid,value)
    update(s,lazy,node*2+1,left,right,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def update_lazy(s,lazy,node,start,end):
    s[node] += lazy[node]
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def query(s,lazy,node,target,start,end):
    if lazy[node] != 0:
        update_lazy(s,lazy,node,start,end)
    if start == end: return s[node]
    mid = (start+end) // 2
    if target <= mid: return query(s,lazy,node*2,target,start,mid)
    else: return query(s,lazy,node*2+1,target,mid+1,end)

def update_rev(s,node,target,start,end,value):
    if start == end:
        s[node] += value
        return
    mid = (start+end) // 2
    if target <= mid: update_rev(s,node*2,target,start,mid,value)
    else: update_rev(s,node*2+1,target,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def query_rev(s,node,left,right,start,end):
    if left > end or start > right: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return query_rev(s,node*2,left,right,start,mid) + query_rev(s,node*2+1,left,right,mid+1,end)

seg = [0] * tree_size
seg_rev = [0] * tree_size
lazy = [0] * tree_size

state = 0

a = [0] * n
for _ in range(m):
    command = list(map(int,input().split()))
    if command[0] == 1:
        i,w = command[1], command[2]
        if state == 0:
            update(seg,lazy,1,ett[i-1][0],ett[i-1][1],0,n-1,w)
        else:
            update_rev(seg_rev,1,ett[i-1][0],0,n-1,w)
        a[i-1] += w
    elif command[0] == 2:
        i = command[1]
        print(query(seg,lazy,1,ett[i-1][0],0,n-1)+query_rev(seg_rev,1,ett[i-1][0],ett[i-1][1],0,n-1))
    else:
        state += 1
        state %= 2