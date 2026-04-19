import sys,math

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    START, END = 0,n-1
    array = get_array(n)
    s_size = 2 ** (math.ceil(math.log2(n))+1)
    max_s, min_s = [0] * s_size, [0] * s_size
    init_max_s_and_min_s(array,max_s,min_s,1,START,END)
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1; b-= 1
        max_value = max_query(max_s,1,a,b,START,END)
        min_value = min_query(min_s,1,a,b,START,END)
        print(min_value,max_value)

def get_array(n):
    array = []
    for _ in range(n): array.append(int(input()))
    return array

def init_max_s_and_min_s(array,max_s,min_s,node,start,end):
    if start == end:
        max_s[node] = array[end]
        min_s[node] = array[end]
        return
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    init_max_s_and_min_s(array,max_s,min_s,l_node,start,mid)
    init_max_s_and_min_s(array,max_s,min_s,r_node,mid+1,end)
    if max_s[l_node] > max_s[r_node]: max_s[node] = max_s[l_node]
    else: max_s[node] = max_s[r_node]
    if min_s[l_node] > min_s[r_node]: min_s[node] = min_s[r_node]
    else: min_s[node] = min_s[l_node]

def max_query(s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    l_node = node*2; r_node = l_node + 1
    mid = (start+end) // 2
    l_max = max_query(s,l_node,left,right,start,mid)
    r_max = max_query(s,r_node,left,right,mid+1,end)
    return max(l_max,r_max)

def min_query(s,node,left,right,start,end):
    if start > right or end < left: return INF
    if left <= start and end <= right: return s[node]
    l_node = node*2; r_node = l_node + 1
    mid = (start+end) // 2
    l_min = min_query(s,l_node,left,right,start,mid)
    r_min = min_query(s,r_node,left,right,mid+1,end)
    return min(l_min,r_min)

if __name__ == "__main__":
    INF = 1000000000
    main()