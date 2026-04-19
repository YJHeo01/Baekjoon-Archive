import sys, math

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    n,k = map(int,input().split())
    array = list(range(n))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    min_s = [INF] * s_length
    max_s = [0] * s_length
    init_min_s(array,min_s,1,0,n-1)
    init_max_s(array,max_s,1,0,n-1)
    for _ in range(k):
        q,a,b = map(int,input().split())
        if q == 0:
            array[a], array[b] = array[b], array[a]
            update_max_s(array,max_s,1,a,0,n-1)
            update_max_s(array,max_s,1,b,0,n-1)
            update_min_s(array,min_s,1,a,0,n-1)
            update_min_s(array,min_s,1,b,0,n-1)
        else:
            min_value = query_min_s(min_s,1,a,b,0,n-1)
            max_value = query_max_s(max_s,1,a,b,0,n-1)
            if min_value != a or max_value != b:
                print("NO")
            else:
                print("YES")

def init_min_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init_min_s(a,s,l_node,start,mid)
    init_min_s(a,s,r_node,mid+1,end)
    s[node] = min(s[l_node],s[r_node])

def init_max_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init_max_s(a,s,l_node,start,mid)
    init_max_s(a,s,r_node,mid+1,end)
    s[node] = max(s[l_node],s[r_node])

def update_min_s(a,s,node,target,start,end):
    if start > target or end < target:
        return
    if start == end:
        s[node] = a[target]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update_min_s(a,s,l_node,target,start,mid)
    update_min_s(a,s,r_node,target,mid+1,end)
    s[node] = min(s[l_node],s[r_node])

def update_max_s(a,s,node,target,start,end):
    if start > target or end < target:
        return
    if start == end:
        s[node] = a[target]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update_max_s(a,s,l_node,target,start,mid)
    update_max_s(a,s,r_node,target,mid+1,end)
    s[node] = max(s[l_node],s[r_node])

def query_min_s(s,node,left,right,start,end):
    if left <= start and end <= right:
        return s[node]
    if start > right or end < left:
        return INF
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return min(query_min_s(s,l_node,left,right,start,mid),query_min_s(s,r_node,left,right,mid+1,end))

def query_max_s(s,node,left,right,start,end):
    if left <= start and end <= right:
        return s[node]
    if start > right or end < left:
        return -1
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return max(query_max_s(s,l_node,left,right,start,mid),query_max_s(s,r_node,left,right,mid+1,end))

if __name__ == "__main__":
    INF = int(1e9)
    main()