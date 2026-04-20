import heapq

n,m,t,d = map(int,input().split())

mountain = []

for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j].isupper() == True:
            tmp[j] = ord(tmp[j]) - ord('A')
        else:
            tmp[j] = ord(tmp[j]) - ord('a') + 26
    mountain.append(tmp)

INF = int(1e9)

hotel_to_mountain_distance = [[INF]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph = [[[]for _ in range(m)]for _ in range(n)]

for vx in range(n):
    for vy in range(m):
        for k in range(4):
            nx = vx + dx[k]
            ny = vy + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or abs(mountain[nx][ny]-mountain[vx][vy]) > t:
                continue
            if mountain[vx][vy] >= mountain[nx][ny]:
                graph[vx][vy].append((nx,ny,1))
            else:
                graph[vx][vy].append((nx,ny,(mountain[nx][ny]-mountain[vx][vy])**2))

def find_HotelToMountain(graph,distance,high_list):
    q = []
    distance[0][0] = 0
    heapq.heappush(q,(0,0,0))
    while q:
        dist, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy]:
            continue
        for nx,ny,length in graph[vx][vy]:
            nd = dist + length
            if distance[nx][ny] > nd and nd <= d:
                high_list[nx][ny] = max(high_list[vx][vy],mountain[nx][ny])
                distance[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))

def find_MountainToHotel(graph,start):
    distance = [[INF]*m for _ in range(n)]
    distance[start[0]][start[1]] = hotel_to_mountain_distance[start[0]][start[1]]
    q = []
    heapq.heappush(q,(hotel_to_mountain_distance[start[0]][start[1]],start[0],start[1]))
    while q:
        dist,vx,vy = heapq.heappop(q)
        if dist > distance[vx][vy]:
            continue
        for nx,ny,length in graph[vx][vy]:
            nd = dist + length
            if distance[nx][ny] > nd and nd <= d:
                distance[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))
    if distance[0][0] <= d:
        return True
    
high_list = [[0]*m for _ in range(n)]
high_list[0][0] = mountain[0][0]

find_HotelToMountain(graph,hotel_to_mountain_distance,high_list)

answer = 0

for i in range(n):
    for j in range(m):
        if high_list[i][j] > answer and find_MountainToHotel(graph,(i,j)) == True:
            answer = high_list[i][j]

print(answer)