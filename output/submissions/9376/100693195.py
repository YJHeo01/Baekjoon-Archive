from collections import deque
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
    queue = deque([])
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '$': continue
            if trash_1 == (-1,-1): trash_1 = (i,j)
            else : trash_2 = (i,j)
    queue = deque([])
    queue.append(trash_1); queue.append(trash_2)
    visited = [[False]*w for _ in range(h)]
    answer = h*w
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= h or ny >= w: return 0
            if visited[nx][ny] or maze[nx][ny] == '#' or maze[nx][ny] == '*': continue
            visited[nx][ny] = True
            queue.append((nx,ny))
    
    for i in range(h):
        if visited[i][w-1] or visited[i][0]:
            answer = 0
            break
    for i in range(w):
        if visited[0][i] or visited[h-1][i]:
            answer = 0
            break
    if answer == 0:
        return answer
    a_dist = [[INF]*w for _ in range(h)]
    a_dist[trash_1[0]][trash_1[1]] = 0
    q = []
    heapq.heappush(q,(0,trash_1[0],trash_1[1]))
    while q:
        cnt,x,y = heapq.heappop(q)
        if a_dist[x][y] > cnt: continue
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
    for x in range(h):
        for y in range(w):
            if maze[x][y] != '#': continue
            tmp = 1
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= h or ny >= w or maze[nx][ny] == '.' or maze[nx][ny] == '$': tmp = 0
            if tmp or (a_dist[x][y] + b_dist[x][y] + 1) >= answer: continue
            answer = min(answer,a_dist[x][y]+b_dist[x][y]+dijk(maze,[[INF]*w for _ in range(h)],(x,y)))
    return answer
            
for _ in range(t):
    print(solution())