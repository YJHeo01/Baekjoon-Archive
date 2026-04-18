import sys

input = sys.stdin.readline
sys.setrecursionlimit(300001)

n = int(input())

parent = [-1] * 300001

arr = list(map(int,input().split()))

root = [-1] * 300001

def find_parent(parent,x):
    if parent[x] == -1: return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b: return
    parent[a]=b

for i in range(n):
    if root[arr[i]] == -1:
        root[arr[i]]=i
    else:
        union_parent(parent,i,root[arr[i]])
        
m = int(input())

for _ in range(m):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x,y = query[1:]
        if root[x]==-1: continue
        if root[y]==-1:
            arr[root[x]]=y
            root[y] = root[x]
        else:
            union_parent(parent,root[x],root[y])
        root[x] = -1
    else:
        z = query[1]
        print(arr[find_parent(parent,z-1)])