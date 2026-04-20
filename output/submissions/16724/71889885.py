import sys

input = sys.stdin.readline

n,m = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(input()))

parent = [[(0,0)]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        parent[i][j] = (i,j)

def find_parent(parent,x):
    if parent[x[0]][x[1]] == (x[0],x[1]):
        return x
    return find_parent(parent,parent[x[0]][x[1]])

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b[0]][b[1]] = a
    else:
        parent[a[0]][a[1]] = b

def search_cycle(graph,parent,start):
    y,x = start
    while 1:
        ny, nx = y, x
        if graph[y][x] == 'U':
            ny -= 1
        elif graph[y][x] == 'D':
            ny += 1
        elif graph[y][x] == 'L':
            nx -= 1
        else:
            nx += 1
        if find_parent(parent,(ny,nx)) == find_parent(parent,(y,x)):
            return
        union_parent(parent,(ny,nx),(y,x))
        y,x = ny, nx

for i in range(n):
    for j in range(m):
        if parent[i][j] == (i,j):
            search_cycle(ground,parent,(i,j))

answer = 0

for i in range(n):
    for j in range(m):
        if parent[i][j] == (i,j):
            answer += 1

print(answer)