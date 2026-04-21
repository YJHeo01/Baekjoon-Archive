import math, sys

input = sys.stdin.readline

n = int(input())

INF = int(1e9)

s_length = 2 ** math.ceil(math.log2(30001)+1)

tree = [[] for _ in range(s_length)]

def update(s,node,left,right,start,end,value):
    if left > end or start > right: return
    if left <= start and end <= right:
        s[node].append(value)
        return
    mid = (start+end) // 2
    update(s,node*2,left,right,start,mid,value)
    update(s,node*2+1,left,right,mid+1,end,value)

def query(s,node,left,right,start,end):
    if left > end or start > right: return []
    if start == end: return s[node]
    mid = (start+end) // 2
    ret_value = s[node] + query(s,node*2+1,left,right,mid+1,end) + query(s,node*2,left,right,start,mid)
    return ret_value

for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    update(tree,1,x1,x2-1,0,30000,(y1,y2))


answer = 0
    
for i in range(30000):
    tmp = query(tree,1,i,i,0,30000)
    tmp.sort()
    start, end = 0,0
    for l,r in tmp:
        if l > end:
            answer += (end-start)
            start = l
            end = r
        else:
            end = max(end,r)
    answer += (end-start)

print(answer)