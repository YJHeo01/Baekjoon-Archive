import sys, math

input = sys.stdin.readline

n,c = map(int,input().split())

arr = [0] + list(map(int,input().split()))

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

s_length = 2 ** math.ceil(math.log2(n)+1)

size = s_length // 2

pos = [[] for _ in range(c+1)]

for i in range(1,n+1):
    pos[arr[i]].append(i)

m = int(input())

answer = [0] * m

querys = []

for idx in range(m):
    i,j = map(int,input().split())
    querys.append((i,j,idx))
    
for color in range(1,c+1):
    s = [0] * s_length
    for i in pos[color]:
        update(s,size,i,1)
    for i,j,idx in querys:
        if answer[idx] != 0: continue
        if query(s,size,i,j) * 2 > (j-i+1):
            answer[idx] = color

ans = []

for i in range(m):
    if answer[i] == 0:
        ans.append("no")
    else:
        ans.append("yes "+str(answer[i]))

sys.stdout.write("\n".join(ans))