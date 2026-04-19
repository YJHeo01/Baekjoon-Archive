import sys, math

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()
def solution():
    n,m = map(int,input().split())
    s_length = 1 << (math.ceil(math.log2(n))+1)
    array = list(range(-1,-n-1,-1))
    INF = int(1e9)
    max_s = [-INF] * s_length
    min_s = [INF] * s_length
    init(array,max_s,min_s,1,0,n-1)
    movie = list(map(int,input().split()))
    for i in range(m):
        idx = movie[i] - 1
        print(query(max_s,min_s,1,0,n-1,array[idx]),end=" ")
        update(max_s,min_s,1,idx,0,n-1,i)
        array[idx] = i
    print()
        

def init(a,max_s,min_s,node,start,end):
    if start == end:
        max_s[node] = a[end]
        min_s[node] = a[end]
        return
    mid = (start+end) // 2
    init(a,max_s,min_s,node*2,start,mid)
    init(a,max_s,min_s,node*2+1,mid+1,end)
    max_s[node] = max(max_s[node*2],max_s[node*2+1])
    min_s[node] = min(min_s[node*2],min_s[node*2+1])
    
def query(max_s,min_s,node,start,end,target):
    if max_s[node] <= target:
        return 0
    if min_s[node] > target:
        return end - start + 1
    mid = (start+end) // 2
    return query(max_s,min_s,node*2,start,mid,target) + query(max_s,min_s,node*2+1,mid+1,end,target)

def update(max_s,min_s,node,target,start,end,value):
    if start > target or end < target: return
    if start == end:
        max_s[node] = value
        min_s[node] = value
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    update(max_s,min_s,l_node,target,start,mid,value)
    update(max_s,min_s,r_node,target,mid+1,end,value)
    max_s[node] = max(max_s[l_node],max_s[r_node])
    min_s[node] = min(min_s[l_node],min_s[r_node])
    
if __name__ == "__main__":
    main()