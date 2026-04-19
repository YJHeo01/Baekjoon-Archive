import sys, math

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    array = [INF] + list(map(int,input().split()))
    s_size = 2 ** (math.ceil(math.log2(n+1))+1)
    s = [0] * s_size
    init(array,s,1,0,n)
    m = int(input())
    for _ in range(m):
        command, i, a = map(int,input().split())
        if command == 1:update(array,s,1,i,0,n,a)
        else: print(query(array,s,1,i,a,0,n))

def init(array,s,node,start,end):
    if start == end:
        s[node] = start
        return
    init(array,s,node*2,start,(start+end)//2)
    init(array,s,node*2+1,(start+end)//2+1,end)
    if array[s[node*2]] > array[s[node*2+1]]: s[node] = s[node*2+1]
    else: s[node] = s[node*2]

def update(array,s,node,target,start,end,value):
    if target < start or target > end: return
    if start == end:
        array[target] = value; s[node] = target
        return
    mid = (start + end) // 2
    l_idx = node * 2; r_idx = l_idx + 1
    update(array,s,l_idx,target,start,mid,value)
    update(array,s,r_idx,target,mid+1,end,value)
    if s[r_idx] < s[l_idx]: s[node] = s[r_idx]
    else: s[node] = s[l_idx]
    
def query(array,s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    l_idx = query(array,s,node*2,left,right,start,mid)
    r_idx = query(array,s,node*2+1,left,right,mid+1,end)
    if array[r_idx] < array[l_idx]: return r_idx
    else: return l_idx

if __name__ == "__main__":
    INF = int(1e9)
    main()