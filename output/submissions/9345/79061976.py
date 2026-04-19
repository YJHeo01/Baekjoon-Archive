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
    init_s(array,max_s,min_s,1,0,n-1)
    for _ in range(k):
        q,a,b = map(int,input().split())
        if q == 0:
            array[a],array[b] = array[b],array[a]
            update(array,max_s,min_s,1,a,b,0,n-1)
        else:
            max_value, min_value = query(max_s,min_s,1,a,b,0,n-1)
            if max_value > b or min_value < a: print("NO")
            else: print("YES")

def init_array(n):
    array = [0] * n
    for i in range(n): array[i] = i
    return array

def init_s(array,max_s,min_s,node,start,end):
    if start == end:
        max_s[node], min_s[node] = array[end], array[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init_s(array,max_s,min_s,l_node,start,mid)
    init_s(array,max_s,min_s,r_node,mid+1,end)
    max_s[node] = max(max_s[r_node],max_s[l_node])
    min_s[node] = min(min_s[l_node],min_s[r_node])

def update(a,max_s,min_s,node,left,right,start,end):
    if start > right or end < left: return
    if start == end:
        min_s[node], max_s[node] = a[end], a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update(a,max_s,min_s,l_node,left,right,start,mid)
    update(a,max_s,min_s,r_node,left,right,mid+1,end)
    min_s[node] = min(min_s[l_node],min_s[r_node])
    max_s[node] = max(max_s[l_node],max_s[r_node])

def query(max_s,min_s,node,left,right,start,end):
    if start > right or end < left: return 0,100001
    if left <= start and end <= right: return max_s[node],min_s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    l_max, l_min = query(max_s,min_s,l_node,left,right,start,mid)
    r_max, r_min = query(max_s,min_s,r_node,left,right,mid+1,end)
    return max(l_max,r_max),min(l_min,r_min)

if __name__ == "__main__":
    main()