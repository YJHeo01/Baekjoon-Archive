from collections import deque

INF = 5000*5000

n, m = map(int,input().split())

def bfs(graph,start):
    queue = deque([start])
    visited = [INF]*(n+1)
    visited[start] = 0
    visited[0] = 0
    while queue:
        vx = queue.popleft()
        for i in graph[vx]:
            if visited[i] > visited[vx] + 1:
                visited[i] = visited[vx] + 1
                queue.append(i)
    return sum(visited)

friend = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)
answer_friend = INF
answer = 0
for i in range(1,n+1):
    f_cnt = bfs(friend,i)
    if answer_friend > f_cnt:
        answer_friend = f_cnt
        answer = i

print(answer)