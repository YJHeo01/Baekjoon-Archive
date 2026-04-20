import heapq

import sys

input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a
    return

n, m = map(int,input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

q = []

for _ in range(m):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(c,a,b))

town_road = 0
answer = 0
for _ in range(m):
    cost,town_1,town_2 = heapq.heappop(q)
    if find_parent(parent,town_1) == find_parent(parent,town_2):
        continue
    union_parent(parent,town_1,town_2)
    answer += cost
    town_road = max(town_road,cost)

print(answer - town_road)