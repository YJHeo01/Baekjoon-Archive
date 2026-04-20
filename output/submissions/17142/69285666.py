from collections import deque

INF = 10000
l = 0
n,m = map(int,input().split())
virus = []
RnD_center = []
for i in range(n):
    tmp = list(map(int,input().split()))
    RnD_center.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            virus.append((i,j))
            l += 1

answer = INF
def bfs(graph,visited,start):
    global answer
    queue = deque([])
    for i in start:
        queue.append(virus[i])
        visited[virus[i][0]][virus[i][1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        v = queue.popleft()
        vx, vy = v[0], v[1]
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[vx][vy] != 1 and visited[nx][ny] > visited[vx][vy]  + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
    new_answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                new_answer = max(new_answer,visited[i][j])


    answer = min(new_answer,answer)



def backtracking(m,answer_list,num_list):
    if len(answer_list) == m:
        visited = [[INF] * n for _ in range(n)]
        bfs(RnD_center,visited,answer_list)
        return 
    for i in num_list:
        if i in answer_list:
            continue
        tmp = answer_list
        tmp.append(i)
        backtracking(m,tmp,num_list)
        tmp.pop()

virus_list = [0] * l

for i in range(1,l):
    virus_list[i] = i

backtracking(m,[],virus_list)

if answer == INF:
    answer = -1
print(answer)