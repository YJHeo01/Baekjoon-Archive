#https://github.com/YJHeo01
#dijkstra
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

hotel_to_mountain_distance = [[INF]*m for _ in range(n)] #호텔에서 산까지의 거리

dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph = [[[]for _ in range(m)]for _ in range(n)]

for vx in range(n):#입력된 산의 지도를 인접 리스트 형식으로 최단 경로를 탐색할 수 있게 변환하고, 알파벳을 숫자로 변환한다. 
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
visited = [[False]*m for _ in range(n)]

def find_HotelToMountain(graph,visited,distance):#호텔에서 산까지의 최단경로를 구한다.
    q = []
    distance[0][0] = 0
    visited[0][0] = True
    heapq.heappush(q,(0,0,0))
    while q:
        dist, vx, vy = heapq.heappop(q)
        if dist > distance[vx][vy]:
            continue
        for nx,ny,length in graph[vx][vy]:
            nd = dist + length
            if distance[nx][ny] > nd and nd <= d:
                visited[nx][ny] = True
                distance[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))

def find_MountainToHotel(graph,start):#해가 지기 전 산에서 호텔까지 도달할 수 있는지 체크
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
    

find_HotelToMountain(graph,visited,hotel_to_mountain_distance)

answer = 0

for i in range(n):
    for j in range(m):
        if mountain[i][j] > answer and visited[i][j] and find_MountainToHotel(graph,(i,j)) == True:
            answer = mountain[i][j] #산 봉우리의 높이가 기존 최댓값보다 높고, 해가 지기 전 산봉우리에 도달했을 경우 산에서 호텔까지 해가 지기 전 도달할 수 있는지 체크하는 함수를 콜 

print(answer)
