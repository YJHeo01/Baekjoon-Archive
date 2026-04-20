import sys,heapq

input = sys.stdin.readline

n = int(input())

edges = []
parent = [0] * n

for i in range(n):
    parent[i] = i

for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(i+1,n):
        heapq.heappush(edges,(tmp[j],i,j))

answer = 0

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

while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)