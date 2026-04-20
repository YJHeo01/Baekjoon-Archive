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

n,m = map(int,input().split())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

connected_component = []
answer = 0

for i in range(1,n+1):
    tmp = find_parent(parent,i)
    if tmp not in connected_component:
        connected_component.append(tmp)
        answer += 1

print(answer)