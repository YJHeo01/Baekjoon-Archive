import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x

def union_parent(parent,a,b):
    a_ = find_parent(parent,a)
    if a_ == 1:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
l = []
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i
for i in range(n-1):
    a,b = map(int,input().split())
    l.append((min(a,b),max(a,b)))

for i in range(n-1):
    union_parent(parent,l[i][0],l[i][1])

for i in range(2,n+1):
    print(parent[i])