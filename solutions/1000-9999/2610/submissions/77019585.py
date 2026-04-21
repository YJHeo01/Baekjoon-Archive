n = int(input())
m = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        find_parent(parent,parent[x])
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

def get_shortest_path_length(graph,visited,start):
    ret_value = 0
    for nx in graph[start]:
        if visited[nx] == False:
            visited[nx] = True
            ret_value = max(ret_value,get_shortest_path_length(graph,visited,nx))
            visited[nx] = False
    ret_value += 1
    return ret_value

time[0] = INF
visited = [False] * (n+1)
for i in range(1,n+1):
    visited[i] = True
    time[i] = get_shortest_path_length(graph,visited,i)
    visited[i] = False

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