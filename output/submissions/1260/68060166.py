from collections import deque
def dfs(start,visited,array):
    print(start, end = ' ')
    visited[start] = True
    for i in array[start]:
        if not visited[i]:
            dfs(i,visited,array)
def bfs(start,visited,array):
    queue = deque([start])
    visited[start] = True
    while(queue):
        v = queue.popleft()
        print(v, end = ' ')
        for i in array[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m, v = map(int,input().split())
visited = [False] * 10002
array = []
for i in range(n+1):
    array.append([])
for i in range(m):
    a, b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)
    
for i in range(m):
    array[i].sort()

dfs(v,visited,array)
visited = [False] * 10002
print()
bfs(v,visited,array)