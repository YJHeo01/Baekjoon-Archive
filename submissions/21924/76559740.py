import sys

input = sys.stdin.readline

n,m = map(int,input().split())

road = []

for _ in range(m):
    a,b,c = map(int,input().split())
    road.append((c,a,b))

road.sort()

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

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

answer = 0

for c,a,b in road:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
    else:
        answer += c

all_connect = True

for i in range(1,n+1):
    if find_parent(parent,i) != 1:
        all_connect = False
        break

if all_connect == False:
    answer = -1

print(answer)