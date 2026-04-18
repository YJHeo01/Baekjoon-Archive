import sys

input = sys.stdin.readline

n,m,t = map(int,input().split())

routers = []

for _ in range(m):
    u,v,s = map(int,input().split())
    routers.append((s,u,v))

routers.append((0,1,1))
routers.append((t,1,1))
routers.sort()


last_time = 0
cnt = n

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

answer = 0

for i in range(1,m+2):
    answer += cnt * (routers[i][0] - routers[i-1][0])
    s,u,v = routers[i]
    if find_parent(parent,u) != find_parent(parent,v):
        cnt -= 1
        union_parent(parent,u,v)

answer -= n
answer += cnt

print(answer)