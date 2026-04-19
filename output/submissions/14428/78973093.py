import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_size = 2 ** (math.ceil(math.log2(n))+1)
    s = [0] * s_size
    init(array,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        c,i,j = map(int,input().split())
        if c == 1:
            array[i-1] = j
            update(array,s,1,i-1,0,n-1)
        else:
            print(query(array,s,1,i-1,j-1,0,n-1) + 1)

def init(array,s,node,start,end):
    if start == end:
        s[node] = start
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    init(array,s,l_node,start,mid)
    init(array,s,r_node,mid+1,end)
    if array[s[l_node]] > array[s[r_node]]: s[node] = s[r_node]
    else: s[node] = s[l_node]

def update(array,s,node,target,start,end):
    if start > target or end < target or start == end: return
    l_node = node*2; r_node = l_node + 1; mid = (start+end) // 2
    update(array,s,l_node,target,start,mid)
    update(array,s,r_node,target,mid+1,end)
    if array[s[l_node]] > array[s[r_node]]: s[node] = s[r_node]
    else: s[node] = s[l_node]

def query(array,s,node,left,right,start,end):
    if start > right or left > end: return -1
    if left <= start and end <= right: return s[node]
    l_node = 2 * node; r_node = l_node + 1
    mid = (start+end) // 2
    l_min = query(array,s,l_node,left,right,start,mid)
    r_min = query(array,s,r_node,left,right,mid+1,end)
    if l_min == -1: return r_min
    if r_min == -1: return l_min
    if array[l_min] > array[r_min]: return r_min
    else: return l_min

if __name__ == "__main__":
    main()