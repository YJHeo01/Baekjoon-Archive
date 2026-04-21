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

s = [[0]*s_length for _ in range(c+1)]

for i in range(1,n+1):
    update(s[arr[i]],size,i,1)

m = int(input())

for idx in range(m):
    answer = 0
    i,j = map(int,input().split())
    full = j - i + 1
    amount = full
    for color in range(1,c+1):
        if amount * 2 <= full: break
        tmp = query(s[color],size,i,j)
        if tmp * 2 > full:
            answer = color
            break
        amount -= tmp
    if answer == 0:
        print("no")
    else:
        print("yes",answer)