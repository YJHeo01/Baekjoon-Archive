import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    s_length = 2 ** (math.ceil(math.log2(n))+1)
    s = [0] * s_length
    init_s(array,s,1,0,n-1)
    m = int(input())
    for _ in range(m):
        a,b,c =  map(int,input().split())
        if a == 1:
            array[b-1] = c
            update_s(array,s,1,b-1,0,n-1)
        elif a == 2:
            print(c-b+1-query_s(s,1,b-1,c-1,0,n-1))
        else:
            print(query_s(s,1,b-1,c-1,0,n-1))

def init_s(a,s,node,start,end):
    if start == end:
        s[node] = a[end] % 2
        return
    mid = (start+end) // 2
    init_s(a,s,node*2,start,mid)
    init_s(a,s,node*2+1,mid+1,end)
    s[node] = s[node*2] + s[node*2+1]

def update_s(a,s,node,target,start,end):
    if start > target or end < target: return
    if start == end:
        s[node] = a[target] % 2
        return
    mid = (start+end) // 2
    update_s(a,s,node*2,target,start,mid)
    update_s(a,s,node*2+1,target,mid+1,end)
    s[node] = s[node*2] + s[node*2+1]

def query_s(s,node,left,right,start,end):
    if left > end or right < start: return 0
    if left <= start and end <= right: return s[node]
    return query_s(s,node*2,left,right,start,(start+end)//2) + query_s(s,node*2+1,left,right,(start+end)//2+1,end)

if __name__ == "__main__":
    main()