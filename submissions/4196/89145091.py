import sys

input = sys.stdin.readline

t = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    parent[b] = a

for _ in range(t):
    n,m = map(int,input().split())
    parent = list(range(n+1))
    for _ in range(m):
        a,b = map(int,input().split())
        if find_parent(parent,b) != b: continue
        union_parent(parent,a,b)
    answer = 0
    for i in range(1,n+1):
        if i == find_parent(parent,i): answer += 1
    print(answer)