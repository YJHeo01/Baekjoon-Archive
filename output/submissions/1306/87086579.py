import math

def main():
    n,m = map(int,input().split())
    s_length = 2 ** math.ceil(math.log2(n)+1)
    s = [-1] * (s_length)
    a = list(map(int,input().split()))
    init(a,s,1,0,n-1)
    for i in range(m-1,n-m+1):
        print(query(s,1,i-(m-1),i+(m-1),0,n-1),end=" ")

def init(a,s,node,start,end):
    if start == end:
        s[node] = a[start]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init(a,s,l_node,start,mid)
    init(a,s,r_node,mid+1,end)
    s[node] = max(s[l_node],s[r_node])

def query(s,node,left,right,start,end):
    if start > right or end < left: return -1
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return max(query(s,l_node,left,right,start,mid),query(s,r_node,left,right,mid+1,end))

if __name__ == "__main__":
    main()