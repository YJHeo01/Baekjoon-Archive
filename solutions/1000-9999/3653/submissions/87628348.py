import sys, math

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    n,m = map(int,input().split())
    s_length = 1 << (math.ceil(math.log2(m+n))+1)
    last_visit = list(range(n-1,-1,-1))
    s = [0] * s_length
    a = [1] * n + [0] * m
    init(a,s,1,0,n+m-1)
    movie = list(map(int,input().split()))
    for i in range(m):
        idx = movie[i] - 1
        update(s,1,last_visit[idx],0,n+m-1,0)
        print(query(s,1,last_visit[idx],n+i,0,n+m-1),end=" ")
        last_visit[idx] = n + i
        update(s,1,last_visit[idx],0,n+m-1,1)
    print()
        
def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return a[end]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    s[node] = (init(a,s,l_node,start,mid) + init(a,s,r_node,mid+1,end))
    return s[node]
    
def query(s,node,left,right,start,end):
    if end < left or start > right: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return query(s,node*2,left,right,start,mid) + query(s,node*2+1,left,right,mid+1,end)


def update(s,node,target,start,end,value):
    if start > target or end < target: return
    if start == end:
        s[node] = value
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    update(s,l_node,target,start,mid,value)
    update(s,r_node,target,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]
    
if __name__ == "__main__":
    main()