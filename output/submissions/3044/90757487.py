from collections import deque
import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

target = [False] * (n+1)

visited = [False] * (n+1)
    
def dfs(graph,visited,target,x):
    for nx in graph[x]:
        if nx == 2:
            target[nx] = True
            target[x] = True
            continue
        target[x] |= target[nx]
        if visited[nx]: continue
        visited[nx] = True
        target[x] |= dfs(graph,visited,target,nx)
        target[x] |= target[nx]
    return target[x]

visited[1] = True
target[1] = True

dfs(graph,visited,target,1)

if target[2] == False:
    print(0)
    exit(0)

indegree = [0] * (n+1)

INF = int(1e9)

dp = [0] * (n+1)

dp[1] = 1

for x in range(n+1):
    if target[x] == False: continue
    for nx in graph[x]:
        indegree[nx] += 1

queue = deque([1])

f = False
while queue:
    x = queue.popleft()
    for nx in graph[x]:
        if target[nx] == False: continue
        indegree[nx] -= 1
        dp[nx] += dp[x]
        if dp[nx] >= INF:
            f = True
            dp[nx] %= INF
        if indegree[nx] < 0:
            print("inf")
            exit(0)
        if indegree[nx] <= 0:
            queue.append(nx)

if dp[2] == 0:
    print('inf')
    exit(0)
    

answer = str(dp[2]%INF)

if f:
    while True:
        if len(answer) >= 9: break
        answer = '0' + answer

print(answer)