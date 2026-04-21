import sys

input = sys.stdin.readline

n,m = map(int,input().split())

roads = []

for _ in range(m+1):
    a,b,c = map(int,input().split())
    roads.append((c,a,b))

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
answer = 0

roads.sort()

for road in roads:
    c,a,b = road
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        if c == 0:
            answer += 1

answer = answer ** 2

roads.reverse()
tmp = 0
for i in range(1,n+1):
    parent[i] = i
for road in roads:
    c,a,b = road
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        if c == 0:
            tmp += 1

tmp = tmp ** 2

answer -= tmp

print(answer)