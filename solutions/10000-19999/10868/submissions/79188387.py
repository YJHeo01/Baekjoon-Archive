import math, sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    array = []
    for _ in range(n):
        array.append(int(input()))
    s_size = 2 ** (1+math.ceil(math.log2(n)))
    s = [0] * s_size
    init(array,s,1,0,n-1)
    for _ in range(m):
        a,b = map(int,input().split())
        answer = query(s,1,a-1,b-1,0,n-1)
        print(answer)

def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    mid = (start+end) // 2
    l_node = 2 * node; r_node = l_node + 1
    init(a,s,l_node,start,mid)
    init(a,s,r_node,mid+1,end)
    s[node] = min(s[l_node],s[r_node])

def query(s,node,left,right,start,end):
    if end < left or start > right: return int(1e9)
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2; l_node = node * 2; r_node = l_node + 1
    l_min = query(s,l_node,left,right,start,mid)
    r_min = query(s,r_node,left,right,mid+1,end)
    return min(l_min,r_min)

if __name__ == "__main__":
    main()