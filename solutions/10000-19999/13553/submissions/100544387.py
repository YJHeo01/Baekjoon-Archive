import sys, math

INF = 100000

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

query_s.sort(key=lambda x:(x[0]//blk,x[1]))

left,right = 1,0

s_length = 2 ** math.ceil(math.log2(100001)+1)
size = s_length//2
s = [0] * s_length

def update(tree, size, pos, value):
    i = size + pos
    tree[i] += value
    i //= 2
    while i >= 1:
        tree[i] = tree[i * 2] + tree[i * 2 + 1]
        i //= 2

def query(tree, size, l, r):
    l += size
    r += size
    res = 0
    while l <= r:
        if l % 2 == 1:
            res += tree[l]
            l += 1
        if r % 2 == 0:
            res += tree[r]
            r -= 1
        l //= 2
        r //= 2

    return res
value = 0

for i,j,idx in query_s:
    while right < j:
        right += 1
        value += query(s,size,max(0,arr[right]-k),min(arr[right]+k,INF))
        update(s,size,arr[right],1)
    while right > j:
        update(s,size,arr[right],-1)
        value -= query(s,size,max(0,arr[right]-k),min(INF,arr[right]+k))
        right -= 1
    while left < i:
        update(s,size,arr[left],-1)
        value -= query(s,size,max(0,arr[left]-k),min(INF,arr[left]+k))
        left += 1
    while left > i:
        left -= 1
        value += query(s,size,max(0,arr[left]-k),min(INF,arr[left]+k))
        update(s,size,arr[left],1)
    answer[idx] = value

print("\n".join(map(str, answer)))