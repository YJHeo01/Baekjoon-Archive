from collections import deque
import sys,heapq

input = sys.stdin.readline

n,m,k = map(int,input().split())

array = [0] + list(map(int,input().split()))

cost_list = []

for i in range(1,n+1):
    heapq.heappush(cost_list,(array[i],i))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

friend = [False] * (n+1)
answer = 0

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                queue.append(nx)
    
while cost_list:
    cost, idx = heapq.heappop(cost_list)
    if friend[idx] == True:
        continue
    if cost > k:
        answer = "Oh no"
        break
    k -= cost
    answer += cost
    bfs(graph,friend,idx)

print(answer)