from collections import deque

import sys

input = sys.stdin.readline
n,l,r = map(int,input().split())

def people_move(graph,visited):
    finish = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                queue = deque([(x,y)])
                united_country = []
                value_sum = 0
                united_country_cnt = 0
                while queue:
                    vx,vy = queue.popleft()
                    for i in range(4):
                        nx = vx + dx[i]
                        ny = vy + dy[i]
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                        value = abs(graph[nx][ny]-graph[vx][vy])
                        if value < l or value > r:
                            continue
                        finish = 0
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            value_sum += graph[nx][ny]
                            united_country_cnt += 1
                            united_country.append((nx,ny))
                            queue.append((nx,ny))
                if united_country_cnt == 0:
                    continue
                next_value = value_sum // united_country_cnt
                for country in united_country:
                    graph[country[0]][country[1]] = next_value
    return finish


country = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    country.append(tmp)
answer = 0
finish = 0
while 1:
    visited = [[0]*n for _ in range(n)]
    finish = people_move(country,visited)
    if finish == 1:
        print(answer)
        break
    answer += 1