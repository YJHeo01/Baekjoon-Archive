n,m = map(int,input().split())

road_list = []

for i in range(n):
    tmp = list(input())
    for j in range(i+1,n):
        if tmp[j] == 'Y':
            road_list.append((i,j))

parent = [0]*n

for i in range(1,n):
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
    return


answer = [0] * n

visited = [[False]*n for _ in range(n)]

for road in road_list:
    a,b = road
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        visited[a][b] = True
        visited[b][a] = True
        answer[a] += 1
        answer[b] += 1
        m -= 1

for road in road_list:
    if m == 0:
        break
    a,b = road
    if visited[a][b] == True:
        continue
    visited[a][b] = True
    visited[b][a] = True
    answer[a] += 1
    answer[b] += 1
    m -= 1

for i in range(1,n):
    if find_parent(parent,i) != 0:
        answer = -1
        break
if m > 0:
    answer = -1
    
if answer == -1:
    print(answer)
else:
    for i in answer:
        print(i,end=" ")