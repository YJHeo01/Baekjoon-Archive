import sys

input = sys.stdin.readline

n,m = map(int,input().split())

information = [0] + list(input().split()) 

road_list = []

for _ in range(m):
    u,v,d = map(int,input().split())
    if information[u] == information[v]:
        continue
    road_list.append((d,u,v))
road_list.sort()

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i
connected_univ = [False] * (n+1)
connected_univ_cnt = 0
answer = 0
for road in road_list:
    distance, u, v = road
    if find_parent(parent,u) != find_parent(parent,v):
        if connected_univ[u] == False:
            connected_univ_cnt += 1
            connected_univ[u] = True
        if connected_univ[v] == False:
            connected_univ_cnt += 1
            connected_univ[v] = True
        union_parent(parent,u,v)
        answer += distance

if connected_univ_cnt != n:
    answer = -1

print(answer)