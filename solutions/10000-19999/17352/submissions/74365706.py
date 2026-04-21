import sys

input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1)

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

for i in range(1,n+1):
    parent[i] = i

for _ in range(n-2):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,n):
    if find_parent(parent,i) != find_parent(parent,n):
        print(i,n)
        break