import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)

match = [0] * (n+1)
visited = [False] * (n+1)

def dfs(x):
    for y in graph[x]:
        if visited[y]: continue
        visited[y] = True
        if match[y] == 0 or dfs(match[y]):
            match[y] = x
            return True
    return False

answer = 0
for i in range(1, n+1):
    visited = [False] * (n+1)
    if dfs(i):
        answer += 1

print(answer)