from collections import deque

n,m,energy = map(int,input().split())

city = []

for _ in range(n):
    city.append(list(map(int,input().split())))

driver = list(map(int,input().split()))
driver[0] -= 1; driver[1] -= 1

complete = [False] * m
customer_list = []

for i in range(m):
    customer_list.append(list(map(int,input().split())))
    for j in range(4):
        customer_list[i][j] -= 1
INF = int(1e9)
def select_customer(graph,complete,start):
    queue = deque([start])
    distance = [[INF]*n for _ in range(n)]
    distance[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
                continue
            if distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))
    ret_idx = -1
    shortest_path = INF
    for i in range(m):
        if complete[i] == True:
            continue
        if distance[customer_list[i][0]][customer_list[i][1]] < shortest_path:
            shortest_path = distance[customer_list[i][0]][customer_list[i][1]]
            ret_idx = i
        elif distance[customer_list[i][0]][customer_list[i][1]] == shortest_path:
            if customer_list[i][0] < customer_list[ret_idx][0] or ((customer_list[i][0] == customer_list[ret_idx][0]) and customer_list[i][1] < customer_list[ret_idx][1]):
                ret_idx = i
        else:
            continue
    return ret_idx,shortest_path

def work_taxi(graph,start,dest):
    queue = deque([start])
    distance = [[INF]*n for _ in range(n)]
    distance[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 1:
                continue
            if distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))
    ret_value = distance[dest[0]][dest[1]]
    if ret_value >= INF:
        ret_value = -1
    return ret_value

def solution(graph,complete,start,energy):
    while True:
        dest = select_customer(graph,complete,start)
        if dest[0] == -1:
            return energy
        elif energy < dest[1] or dest[1] >= INF:
            return -1
        else:
            energy -= dest[1]
        tmp = work_taxi(graph,customer_list[dest[0]][:2],customer_list[dest[0]][2:])
        if tmp == -1:
            return -1
        energy -= tmp
        if energy < 0:
            return -1
        energy += (tmp*2)
        complete[dest[0]] = True
        start = customer_list[dest[0]][2:]

print(solution(city,complete,driver,energy))