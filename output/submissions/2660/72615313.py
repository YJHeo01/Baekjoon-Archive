from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
INF = int(1e9)
score_list = [INF] * (n+1)
while True:
    a,b = map(int,input().split())
    if a == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def get_member_score(graph,start):
    queue = deque([start])
    visited = [INF] * (n+1)
    visited[start] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] > visited[vx] + 1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return max(visited[1:])

for i in range(n,0,-1):
    score_list[i] = get_member_score(graph,i)

president_score = min(score_list)

second_line_answer = []

cnt = 0

for i in range(1,n+1):
    if score_list[i] == president_score:
        cnt+=1
        second_line_answer.append(i)

print(president_score,cnt)
for i in second_line_answer:
    print(i,end=" ")