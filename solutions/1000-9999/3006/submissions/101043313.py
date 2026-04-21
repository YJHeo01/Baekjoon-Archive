import sys, math

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

pos = [0] * (n+1)

for i in range(n):
    pos[arr[i]] = i
    
s_length = 1 << math.ceil(math.log2(n)+1)

s = [0] * s_length

size = s_length // 2

def init(s,size,idx):
    node = size + idx
    s[size+idx] += 1
    node //= 2
    while node:
        s[node] = s[node*2] + s[node*2+1]
        node //= 2
        
def update(s,size,idx):
    node = size + idx
    s[size+idx] = 0
    node //= 2
    while node:
        s[node] = s[node*2] + s[node*2+1]
        node //= 2
        
def query(s,node,left,right,start,end):
    if left <= start and end <= right: return s[node]
    if left > end or start > right: return 0
    mid = (start+end) // 2
    return query(s,node*2,left,right,start,mid) + query(s,node*2+1,left,right,mid+1,end)

for i in range(n):
    init(s,size,i)

for i in range(1,n+1):
    if i % 2 == 1:
        x = pos[i//2+1]
        print(query(s,1,0,x-1,0,size-1))
    else:
        x = pos[n-i//2+1]
        print(query(s,1,x+1,n-1,0,size-1))
    update(s,size,x)
