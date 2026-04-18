import sys, math

INF = 200000

input = sys.stdin.readline

n,q = map(int,input().split())

arr = [0] + list(map(int,input().split()))

for i in range(1,n+1):
    arr[i] += 100000

answer = [0] * q

query_s = []

for idx in range(q):
    i,j = map(int,input().split())
    query_s.append((i,j,idx))

blk = int(math.sqrt(n))

query_s.sort(key=lambda x:(x[0]//blk,x[1] if (x[0] // blk) & 1 == 0 else -x[1]))

left,right = 1,0

s_length = 2 ** math.ceil(math.log2(200001)+1)
size = s_length//2
s = [0] * s_length

def update(tree, size, pos, value):
    i = size + pos
    tree[i] += value
    i //= 2
    while i >= 1:
        tree[i] = max(tree[i * 2],tree[i * 2 + 1])
        i //= 2

def query(tree, size, l, r):
    l += size
    r += size
    res = 0
    while l <= r:
        if l % 2 == 1:
            res = max(res,tree[l])
            l += 1
        if r % 2 == 0:
            res = max(res,tree[r])
            r -= 1
        l //= 2
        r //= 2
    return res

value = 0

for i,j,idx in query_s:
    while right < j:
        right += 1
        update(s,size,arr[right],1)
    while right > j:
        update(s,size,arr[right],-1)
        right -= 1
    while left < i:
        update(s,size,arr[left],-1)
        left += 1
    while left > i:
        left -= 1
        update(s,size,arr[left],1)
    answer[idx] = query(s,size,0,INF)

print("\n".join(map(str, answer)))