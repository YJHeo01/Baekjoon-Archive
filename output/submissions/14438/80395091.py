import math, sys

input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    s = [INF] * s_length
    init_segtree(a,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        c,i,j = map(int,input().split())
        if c == 1:
            a[i-1] = j
            update(a,s,1,i-1,0,n-1)
        else: print(smallest_value(s,1,i-1,j-1,0,n-1))


def init_segtree(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return s[node]
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    s[node] = min(init_segtree(a,s,l_node,start,mid),init_segtree(a,s,r_node,mid+1,end))
    return s[node]

def smallest_value(s,node,left,right,start,end):
    if start > right or end < left: return INF
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1; mid = (start+end) // 2
    return min(smallest_value(s,l_node,left,right,start,mid),smallest_value(s,r_node,left,right,mid+1,end))
    
def update(a,s,node,target,start,end):
    if start > target or end < target: return s[node]
    if start == end:
        s[node] = a[target]
        return s[node]
    l_node = node * 2; r_node = l_node + 1; mid = (start+end) // 2
    s[node] = min(update(a,s,l_node,target,start,mid),update(a,s,r_node,target,mid+1,end))
    return s[node]
    
if __name__ == "__main__":
    INF = int(1e9) + 1
    main()