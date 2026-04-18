import sys, heapq

input = sys.stdin.readline

t = int(input())

h,w = 0,0
INF = int(1e9)

def dijk(graph,distance,start):
    ret_value = INF
    distance[start[0]][start[1]] = 0
    q = []
    heapq.heappush(q,(0,start[0],start[1]))
    while q:
        cnt, x, y = heapq.heappop(q)
        if cnt > distance[x][y]: continue
        if graph[x][y] == '#': cnt += 1
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                ret_value = min(ret_value,cnt)
                continue
            if graph[nx][ny] == '*' or cnt >= distance[nx][ny]: continue
            distance[nx][ny] = cnt
            heapq.heappush(q,(cnt,nx,ny))       
    return ret_value
    
def solution():
    global h,w
    h,w = map(int,input().split())
    maze = []
    for _ in range(h):
        maze.append(list(input().rstrip()))
    trash_1 = (-1,-1)
    trash_2 = (-1,-1)
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '$': continue
            if trash_1 == (-1,-1): trash_1 = (i,j)
            else : trash_2 = (i,j)
    answer = h*w
    a_dist = [[INF]*w for _ in range(h)]
    a_dist[trash_1[0]][trash_1[1]] = 0
    q = []
    heapq.heappush(q,(0,trash_1[0],trash_1[1]))
    while q:
        cnt,x,y = heapq.heappop(q)
        if cnt > a_dist[x][y]: continue
        if maze[x][y] == '#':cnt+=1
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if maze[nx][ny] == '*' or cnt >= a_dist[nx][ny]: continue
            a_dist[nx][ny] = cnt
            heapq.heappush(q,(cnt,nx,ny))
    heapq.heappush(q,(0,trash_2[0],trash_2[1]))
    b_dist = [[INF]*w for _ in range(h)]
    b_dist[trash_2[0]][trash_2[1]] = 0
    while q:
        cnt,x,y = heapq.heappop(q)
        if cnt > b_dist[x][y]: continue
        if maze[x][y] == '#':cnt+=1
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if maze[nx][ny] == '*' or cnt >= b_dist[nx][ny]: continue
            b_dist[nx][ny] = cnt
            heapq.heappush(q,(cnt,nx,ny))
    c_dist = [[INF]*w for _ in range(h)]
    for i in [0,h-1]:
        for j in range(w):
            if maze[i][j] == '*': continue
            if maze[i][j] == '#':
                c_dist[i][j] = 1
                heapq.heappush(q,(1,i,j))
            else:
                c_dist[i][j] = 0
                heapq.heappush(q,(0,i,j))
    for i in range(h):
        for j in [0,w-1]:
            if maze[i][j] == '*': continue
            if maze[i][j] == '#':
                c_dist[i][j] = 1
                heapq.heappush(q,(1,i,j))
            else:
                c_dist[i][j] = 0
                heapq.heappush(q,(0,i,j))
    while q:
        cnt,x,y = heapq.heappop(q)
        if cnt > c_dist[x][y]: continue
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w or maze[nx][ny] == '*': continue
            nd = cnt
            if maze[nx][ny] == '#': nd += 1
            if c_dist[nx][ny] > nd:
                c_dist[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny)) 
    for x in range(h):
        for y in range(w):
            answer = min(answer,a_dist[x][y]+b_dist[x][y]+c_dist[x][y])
    return answer
            
for _ in range(t):
    print(solution())