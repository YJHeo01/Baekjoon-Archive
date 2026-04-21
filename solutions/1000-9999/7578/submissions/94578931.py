import math, heapq

n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

idx_list = [-1] * 1000000

for i in range(n):
    idx_list[A[i]] = i
    A[i] = i

q = []

for i in range(n):
    B[i] = idx_list[B[i]]
    heapq.heappush(q,(B[i],i))

length = 2 ** math.ceil(math.log2(n)+1)

seg = [0] * length

def update(s,node,target,start,end):
    if target > end or target < start: return
    if start == end:
        s[node] += 1
        return
    mid = (start+end) // 2
    update(s,node*2,target,start,mid)
    update(s,node*2+1,target,mid+1,end)
    s[node] = s[node*2] + s[node*2+1]

def query(s,node,left,right,start,end):
    if left > end or right < start: return 0
    if start <= left and right <= end: return s[node]
    mid = (start+end) // 2
    return query(s,node*2,left,right,start,mid) + query(s,node*2+1,left,right,mid+1,end)

answer = 0

while q:
    A_idx, B_idx = heapq.heappop(q)
    if A_idx < B_idx:
        update(seg,1,B_idx,0,n-1)
    else:
        answer += query(seg,1,B_idx+1,n-1,0,n-1)

print(answer)