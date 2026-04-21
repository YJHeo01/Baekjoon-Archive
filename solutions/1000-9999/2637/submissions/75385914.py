from collections import deque

n = int(input())
m = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
standard_item = [True] * (n+1)

for _ in range(m):
    x,y,k = map(int,input().split())
    graph[x].append((y,k))
    indegree[y] += 1
    standard_item[x] = False

item_cnt = [0] * (n+1)

def topology_sort(graph,indegree,item_cnt):
    queue = deque([])
    for i in range(1,n+1):
        if indegree[i] == 0:
            item_cnt[i] = 1
            queue.append(i)
    while queue:
        vx = queue.popleft()
        for nx, cnt in graph[vx]:
            indegree[nx] -= 1
            item_cnt[nx] += cnt * item_cnt[vx]
            if indegree[nx] == 0:
                queue.append(nx)

topology_sort(graph,indegree,item_cnt)

for i in range(1,n+1):
    if standard_item[i] == True:
        print(i,item_cnt[i])