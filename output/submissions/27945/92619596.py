import sys, heapq

input = sys.stdin.readline

n,m = map(int,input().split())

edges = []

for _ in range(m):
    u,v,t = map(int,input().split())
    heapq.heappush(edges,(t,u,v))

answer = 1

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

while edges:
    t,u,v = heapq.heappop(edges)
    if t > answer: break
    if find_parent(parent,u) == find_parent(parent,v): continue
    union_parent(parent,u,v)
    answer = t + 1
    
print(answer)