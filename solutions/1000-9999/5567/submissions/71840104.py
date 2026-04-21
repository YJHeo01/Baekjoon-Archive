import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[1] = True
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0

for i in graph[1]:
    for j in graph[i]:
        if visited[j] == False:
            visited[j] = True
            answer += 1

print(answer)