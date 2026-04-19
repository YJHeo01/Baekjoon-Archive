from collections import deque
from itertools import permutations

n,m = map(int,input().split())

item_cnt = 0

house = []

item_list = []
start = (-1,-1)
end = (-1,-1)

for i in range(m):
    tmp = list(input())
    house.append(tmp)
    for j in range(n):
        if tmp[j] == 'X':
            item_cnt += 1
            item_list.append((i,j))
        elif tmp[j] == 'S':
            start = (i,j)
            item_cnt += 1
        elif tmp[j] == 'E':
            end = (i,j)
            item_cnt += 1
        else:
            continue
item_list = [start] + item_list + [end]
INF = int(1e9)

adj_matrix = []

def check_distance(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == '#':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

for item in item_list:
    distance = [[INF]*n for _ in range(n)]
    check_distance(house,distance,item)
    tmp = []
    for x,y in item_list:
        tmp.append(distance[x][y])
    adj_matrix.append(tmp)

data = []
for i in range(1,item_cnt-1):
    data.append(i)

test_case_list = list(permutations(data,item_cnt-2))

answer = INF
for test_case in test_case_list:
    tmp = adj_matrix[0][test_case[0]] + adj_matrix[test_case[-1]][item_cnt-1]
    for idx in range(0,item_cnt-3):
        tmp += adj_matrix[test_case[idx]][test_case[idx+1]]
    answer = min(answer,tmp)

print(answer)
