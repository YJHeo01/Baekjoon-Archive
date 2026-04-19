import sys

input = sys.stdin.readline

n,m = map(int,input().split())

parent = list(range(n+1))

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
        
for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

arr = list(map(int,input().split()))

answer = 0

for i in range(1,n):
    if find_parent(parent,arr[i-1]) != find_parent(parent,arr[i]): answer += 1

print(answer)