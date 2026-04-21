import sys, math

input = sys.stdin.readline

n,k = map(int,input().split())

arr = [0] + list(map(int,input().split()))

m = int(input())

answer = [0] * m

query_s = []

for idx in range(m):
    i,j = map(int,input().split())
    query_s.append((i,j,idx))

blk = int(math.sqrt(n))

query_s.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1]))

left,right = 1,0

s_length = 2 ** math.ceil(math.log2(100001)+1)

s = [0] * s_length

def update(s,node,target,start,end,value):
    if target < start or target > end: return
    if start == end and target == start:
        s[node] += value
        return
    mid = (start+end) // 2
    update(s,node*2,target,start,mid,value)
    update(s,node*2+1,target,mid+1,end,value)
    s[node] = s[node*2] + s[node*2+1]

def query(s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    mid = (start+end) // 2
    return query(s,node*2,left,right,start,mid) + query(s,node*2+1,left,right,mid+1,end)

value = 0

for i,j,idx in query_s:
    while right < j:
        right += 1
        value += query(s,1,arr[right]-k,arr[right]+k,0,100000)
        update(s,1,arr[right],0,100000,1)
    while right > j:
        update(s,1,arr[right],0,100000,-1)
        value -= query(s,1,arr[right]-k,arr[right]+k,0,100000)
        right -= 1
    while left < i:
        update(s,1,arr[left],0,100000,-1)
        value -= query(s,1,arr[left]-k,arr[left]+k,0,100000)
        left += 1
    while left > i:
        left -= 1
        value += query(s,1,arr[left]-k,arr[left]+k,0,100000)
        update(s,1,arr[left],0,100000,1)
    answer[idx] = value

for i in answer:
    print(i)