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

while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0:
        break

    roads = []

    parent = [0] * (m+1)

    for i in range(1,m+1):
        parent[i] = i
    answer = 0
    for _ in range(n):
        x,y,z = map(int,input().split())
        roads.append((z,x,y))
    roads.sort()

    for road in roads:
        distance,x,y = road
        if find_parent(parent,x) != find_parent(parent,y):
            union_parent(parent,x,y)
        else:
            answer += distance

    print(answer) 
