from itertools import combinations
from collections import deque

n, m = map(int,input().split())

city = []

chicken = []

for i in range(n):
    city_row = list(map(int,input().split()))
    for j in range(n):
        if city_row[j] == 2:
            chicken.append((i,j))
    city.append(city_row)

test_case_list = list(combinations(chicken,m))
INF = int(1e9)

def bfs(graph,start):
    distacne_list = [[INF]*n for _ in range(n)]
    ret_value = 0
    queue = deque(start)
    for point in start:
        distacne_list[point[0]][point[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        vx, vy = queue.popleft()
        new_distance = distacne_list[vx][vy] + 1
        for i in range(4):
            nx,ny = vx+dx[i],vy+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if distacne_list[nx][ny] > new_distance:
                distacne_list[nx][ny] = new_distance
                queue.append((nx,ny))
                if graph[nx][ny] == 1:
                    ret_value += new_distance
    return ret_value


answer = INF

for test_case in test_case_list:
    answer = min(answer,bfs(city,test_case))

print(answer)