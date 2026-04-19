import sys, math

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    length = 1 << math.ceil(math.log2(n)+1)
    seg = [0] * length
    lazy = [0] * length
    for _ in range(m):
        o,s,t = map(int,input().split())
        s -= 1; t -= 1
        if o == 0:
            update_seg(seg,lazy,1,s,t,0,n-1)
        else:
            print(query(seg,lazy,1,s,t,0,n-1))

def update_seg(s,lazy,node,left,right,start,end):
    update_lazy(s,lazy,node,start,end)
    if end < left or start > right: return s
    if left <= start and end <= right: 
        lazy[node] += 1
        update_lazy(s,lazy,node,start,end)
        return
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    update_seg(s,lazy,l_node,left,right,start,mid)
    update_seg(s,lazy,r_node,left,right,mid+1,end)
    s[node] = s[l_node] + s[r_node]
    return 
    
def update_lazy(s,lazy,node,start,end):
    lazy[node] %= 2
    if lazy[node] == 0: return
    s[node] = (end-start+1) - s[node]
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0
    
def query(s,lazy,node,left,right,start,end):
    update_lazy(s,lazy,node,start,end)
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    l_node, r_node = node * 2, node * 2 + 1
    return query(s,lazy,l_node,left,right,start,mid) + query(s,lazy,r_node,left,right,mid+1,end)
    
if __name__ == "__main__":
    main()