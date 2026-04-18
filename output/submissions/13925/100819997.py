import sys, math, heapq

input = sys.stdin.readline

MOD = int(1e9) + 7

def main():
    tree = [0] * (2 * tree_size)
    lazy = [[]for _ in range(2*tree_size)]
    for i in range(n):
        init(tree,i)
    m = int(input())
    for i in range(m):
        t, *tmp = map(int,input().split())
        if t == 4:
            x,y = tmp
            print(query(tree,lazy,1,x-1,y-1,0,n-1)%MOD)
        else:
            x,y,v = tmp
            command = (i,t,v)
            update(tree,lazy,1,x-1,y-1,0,n-1,command)

def init(tree,i):
    tree[i+tree_size] += a[i]
    i += tree_size
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def update_lazy(tree,lazy,node,start,end):
    while lazy[node]:
        order,c,v = heapq.heappop(lazy[node])
        if c == 1: tree[node] += v
        elif c == 2: tree[node] *= v
        else: tree[node] = v * (end-start+1)
        tree[node] %= MOD
        if start != end:
            heapq.heappush(lazy[node*2],(order,c,v))
            heapq.heappush(lazy[node*2+1],(order,c,v))

def update(tree,lazy,node,left,right,start,end,command):
    if lazy[node] != []:
        update_lazy(tree,lazy,node,start,end)
    if start > right or end < left: return
    if left <= start and end <= right:
        heapq.heappush(lazy[node],command)
        update_lazy(tree,lazy,node,start,end)
        return
    mid = (start+end) // 2
    update(tree,lazy,node*2,left,right,start,mid,command)
    update(tree,lazy,node*2+1,left,right,mid+1,end,command)
    tree[node] = (tree[node*2] + tree[node*2+1]) % MOD

def query(tree, lazy, node, left, right, start, end):
    if lazy[node] != []:
        update_lazy(tree,lazy,node,start,end)
    if start > right or end < left: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start+end) // 2
    return (query(tree,lazy,node*2,left,right,start,mid) + query(tree,lazy,node*2+1,left,right,mid+1,end)) % MOD

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    tree_size = 2 ** math.ceil(math.log2(n))
    main()