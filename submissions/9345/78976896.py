import sys,math

input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        solution()

def solution():
    n,k = map(int,input().split())
    array = init_array(n)
    s_size = 2 ** (1+math.ceil(math.log2(n)))
    max_s, min_s = [0] * s_size, [0] * s_size
    init_max_s(array,max_s,1,0,n-1)
    init_min_s(array,min_s,1,0,n-1)
    for _ in range(k):
        q,a,b = map(int,input().split())
        if q == 0:
            if a == b:continue
            array[a],array[b] = array[b],array[a]
            update_min_s(array,min_s,1,a,b,0,n-1)
            update_max_s(array,max_s,1,a,b,0,n-1)
        else:
            if a == b: print("YES")
            elif query_min(min_s,1,a,b,0,n-1) < a or query_max(max_s,1,a,b,0,n-1) > b: print("NO")
            else: print("YES")

def init_array(n):
    array = [0] * n
    for i in range(n): array[i] = i
    return array

def init_max_s(array,s,node,start,end):
    if start == end:
        s[node] = array[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init_max_s(array,s,l_node,start,mid)
    init_max_s(array,s,r_node,mid+1,end)
    s[node] = max(s[r_node],s[l_node])

def init_min_s(array,s,node,start,end):
    if start == end:
        s[node] = array[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init_min_s(array,s,l_node,start,mid)
    init_min_s(array,s,r_node,mid+1,end)
    s[node] = min(s[l_node],s[r_node])

def update_min_s(a,s,node,left,right,start,end):
    if start > right or end < left: return
    if start == end:
        s[node] = a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update_min_s(a,s,l_node,left,right,start,mid)
    update_min_s(a,s,r_node,left,right,mid+1,end)
    s[node] = min(s[l_node],s[r_node])

def update_max_s(a,s,node,left,right,start,end):
    if start > right or end < left: return
    if start == end:
        s[node] = a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update_max_s(a,s,l_node,left,right,start,mid)
    update_max_s(a,s,r_node,left,right,mid+1,end)
    s[node] = max(s[l_node],s[r_node])

def query_min(s,node,left,right,start,end):
    if start > right or end < left: return 100001
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    l_min = query_min(s,l_node,left,right,start,mid)
    r_min = query_min(s,r_node,left,right,mid+1,end)
    return min(l_min,r_min)

def query_max(s,node,left,right,start,end):
    if start > right or end < left: return -1
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    l_max = query_max(s,l_node,left,right,start,mid)
    r_max = query_max(s,r_node,left,right,mid+1,end)
    return max(l_max,r_max)

if __name__ == "__main__":
    main()