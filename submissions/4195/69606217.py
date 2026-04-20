import sys

input = sys.stdin.readline

SIZE = 100000
def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())

for _ in range(t):
    f = int(input())
    parent = [0] * (SIZE)
    friends = []
    for i in range(SIZE):
        parent[i] = i
    for _ in range(f):
        answer = 0
        a,b = input().split()
        l = len(friends)
        idx = 0
        for i in list(a):
            idx *= 10
            idx += (ord(i) - ord('A'))            
            idx %= SIZE
        a = idx
        idx = 0
        if a not in friends:
            friends.append(a)
        for i in list(b):
            idx *= 10
            idx += (ord(i) - ord('A'))
            idx %= SIZE
        b = idx
        if b not in friends:
            friends.append(b)
        union_parent(parent,a,b)
        f_idx = find_parent(parent,a)
        for i in friends:
            if f_idx == find_parent(parent,i):
                answer += 1
        print(answer)