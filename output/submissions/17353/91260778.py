import sys, math

input = sys.stdin.readline

def main():
    a = list(map(int,input().split()))
    q = int(input())
    for _ in range(q):
        tmp = list(map(int,input().split()))
        if tmp[0] == 1:
            update(cnt,lazy_cnt,1,tmp[1]-1,tmp[2]-1,0,n-1,1)
            update(tree,lazy_tree,1,tmp[1]-1,tmp[2]-1,0,n-1,tmp[1]-1)
        else:
            answer = a[tmp[1]-1]
            tmp_cnt = query(cnt,lazy_cnt,1,tmp[1]-1,0,n-1)
            answer += tmp_cnt
            answer += ((tmp[1]-1) * tmp_cnt - query(tree,lazy_tree,1,tmp[1]-1,0,n-1))
            print(answer)
            
            
def update(tree,lazy,node,left,right,start,end,value):
    if lazy[node] != 0:
        update_lazy(tree,lazy,node,start,end)
    if start > right or end < left: return
    if left <= start and end <= right:
        tree[node] += value
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    mid = (start+end) // 2
    update(tree,lazy,node*2,left,right,start,mid,value)
    update(tree,lazy,node*2+1,left,right,mid+1,end,value)
    tree[node] = tree[node*2] + tree[node*2+1]
        
def update_lazy(tree,lazy,node,start,end):
    tree[node] += lazy[node]
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def query(tree,lazy,node,target,start,end):
    if lazy[node] != 0:
        update_lazy(tree,lazy,node,start,end)
    if start == end: return tree[node]
    mid = (start+end) // 2
    if target <= mid: return query(tree,lazy,node*2,target,start,mid)
    else: return query(tree,lazy,node*2+1,target,mid+1,end)

if __name__ == "__main__":
    n = int(input())
    tree_size = 2 ** math.ceil(math.log2(n))
    tree = [0] * (2 * tree_size)
    cnt = [0] * (2 * tree_size)
    lazy_tree = [0] * (2 * tree_size)
    lazy_cnt = [0] * (2 * tree_size)
    main()