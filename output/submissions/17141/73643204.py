from collections import deque
from itertools import combinations
n,m = map(int,input().split())

virus = []

graph = []

blank_cnt = n**2

for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            virus.append((i,j))
        elif tmp[j] == 1:
            blank_cnt -= 1
        else:
            continue

test_case_list = list(combinations(virus,m))

INF = int(1e9)
answer = INF

def solution(graph,visited,start):
    queue = deque(start)
    for x,y in start:
        visited[x][y] = 0
    virus_cnt = m
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                ret_value = max(visited[nx][ny],ret_value)
                virus_cnt += 1
                queue.append((nx,ny))
    if virus_cnt < blank_cnt:
        ret_value = INF
    return ret_value

for test_case in test_case_list:
    visited = [[INF]*n for _ in range(n)]
    answer = min(solution(graph,visited,test_case),answer)

if answer >= INF:
    answer = -1

print(answer)