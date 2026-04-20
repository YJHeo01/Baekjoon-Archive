import math, sys

input = sys.stdin.readline

n = int(input())

INF = int(1e9)

s_length = 2 ** math.ceil(math.log2(30001)+1)

min_high = [INF] * s_length
max_high = [-1] * s_length

min_lazy = [INF] * s_length
max_lazy = [-1] * s_length

def update_lazy_min(s,node,lazy,start,end):
    s[node] = min(s[node],lazy[node])
    if start != end:
        lazy[node*2] = min(lazy[node],lazy[node*2])
        lazy[node*2+1] = min(lazy[node],lazy[node*2+1])
    lazy[node] = INF

def update_lazy_max(s,node,lazy,start,end):
    s[node] = max(s[node],lazy[node])
    if start != end:
        lazy[node*2] = max(lazy[node*2],lazy[node])
        lazy[node*2+1] = max(lazy[node*2+1],lazy[node])
    lazy[node] = -1
    
def update_max_s(s,lazy,node,left,right,start,end,value):
    if lazy[node] != -1:
        update_lazy_max(s,node,lazy,start,end)
    if left > end or start > right: return
    if left <= start and end <= right:
        s[node] = max(s[node],value)
        if start != end:
            lazy[node*2] = max(lazy[node*2],value)
            lazy[node*2+1] = max(lazy[node*2+1],value)
        return
    mid = (start+end) // 2
    update_max_s(s,lazy,node*2,left,right,start,mid,value)
    update_max_s(s,lazy,node*2+1,left,right,mid+1,end,value)
    s[node] = max(s[node*2],s[node*2+1])


def update_min_s(s,lazy,node,left,right,start,end,value):
    if lazy[node] != INF:
        update_lazy_min(s,node,lazy,start,end)
    if left > end or start > right: return
    if left <= start and end <= right:
        s[node] = min(s[node],value)
        if start != end:
            lazy[node*2] = min(lazy[node*2],value)
            lazy[node*2+1] = min(lazy[node*2+1],value)
        return
    mid = (start+end) // 2
    update_min_s(s,lazy,node*2,left,right,start,mid,value)
    update_min_s(s,lazy,node*2+1,left,right,mid+1,end,value)
    s[node] = min(s[node*2],s[node*2+1])

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    update_max_s(max_high,max_lazy,1,x1,x2-1,0,30000,y2)
    update_min_s(min_high,min_lazy,1,x1,x2-1,0,30000,y1)
    
def max_query(s,lazy,node,left,right,start,end):
    if lazy[node] != -1:
        update_lazy_max(s,node,lazy,start,end)
    if left > end or start > right: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return max(max_query(s,lazy,node*2,left,right,start,mid),max_query(s,lazy,node*2+1,left,right,mid+1,end))

def min_query(s,lazy,node,left,right,start,end):
    if lazy[node] != INF:
        update_lazy_min(s,node,lazy,start,end)
    if left > end or start > right: return INF
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return min(min_query(s,lazy,node*2,left,right,start,mid),min_query(s,lazy,node*2+1,left,right,mid+1,end))

    
answer = 0
    
for i in range(30001):
    max_value = max_query(max_high,max_lazy,1,i,i,0,30000)
    min_value = min_query(min_high,min_lazy,1,i,i,0,30000)
    if min_value > max_value: continue
    answer += (max_value-min_value)

print(answer) 