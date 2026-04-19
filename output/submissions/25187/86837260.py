import sys

input = sys.stdin.readline

n,m,q = map(int,input().split())

array = [0] + list(map(int,input().split()))

clean_water = [0] * (n+1)
dirty_water = [0] * (n+1)

for i in range(1,n+1):
    if array[i] == 1:
        clean_water[i] += 1
    else:
        dirty_water[i] += 1

parent = list(range(n+1))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(clean_water,dirty_water,parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b: return
    if a < b:
        parent[b] = a
        clean_water[a] += clean_water[b]
        dirty_water[a] += dirty_water[b]
    else:
        parent[a] = b
        clean_water[b] += clean_water[a]
        dirty_water[b] += dirty_water[a]

for _ in range(m):
    u,v = map(int,input().split())
    union_parent(clean_water,dirty_water,parent,u,v)

for _ in range(q):
    k = int(input())
    idx = find_parent(parent,k)
    if clean_water[idx] > dirty_water[idx]:
        print(1)
    else:
        print(0)
