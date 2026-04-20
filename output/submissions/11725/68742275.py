import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
     a_ = find_parent(parent,a)


    if a_ == 1:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for i in range(n-1):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

for i in range(2,n+1):
    print(parent[i])