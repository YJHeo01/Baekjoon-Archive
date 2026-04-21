from collections import deque

n = int(input())
m = int(input())

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
    
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    graph[a].append(b)
    graph[b].append(a)

time = [0] * (n+1)

INF = int(1e9)

def get_shortest_path_length(graph,start):
    queue = deque([start])
    ret_value = 0
    length = [INF] * (n+1)
    length[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if length[nx] > length[vx] + 1:
                length[nx] = length[vx] + 1
                ret_value = length[nx]
                queue.append(nx)
    return ret_value

time[0] = INF

for i in range(1,n+1):
    time[i] = get_shortest_path_length(graph,i)

chairman_list = [0] * (n+1)

for i in range(1,n+1):
    idx = find_parent(parent,i)
    if time[chairman_list[idx]] > time[i]:
        chairman_list[idx] = i

answer = []

for i in range(1,n+1):
    if chairman_list[i] == 0:
        continue
    answer.append(chairman_list[i])

answer.sort()
print(len(answer))
for i in answer:
    print(i)