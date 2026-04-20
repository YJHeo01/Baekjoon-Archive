import sys

input = sys.stdin.readline

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
    parent = [0] * (2*f)
    friends = []
    for i in range(2*f):
        parent[i] = i
    for _ in range(f):
        answer = 0
        a,b = input().split()
        l = len(friends)
        for i in range(l):
            if friends[i] == a:
                a = i
                break
        for i in range(l):
            if friends[i] == b:
                b = i
                break
        if type(a) != int:
            friends.append(a)
            a = l
            l += 1
        if type(b) != int:
            friends.append(b)
            b = l
            l += 1
        union_parent(parent,a,b)
        f_idx = find_parent(parent,a)
        for i in range(l):
            if f_idx == find_parent(parent,i):
                answer += 1
        print(answer)