from collections import deque
import sys

input = sys.stdin.readline

def main():
    
    sea = get_sea()
    island_list = []
    idx = 0
    
    for i in range(n):
        for j in range(m):
            if sea[i][j] == 'x':
                island_list.append(get_island_area(sea,(i,j),idx))
                idx += 1
    
    if idx == 0:
        print(-1)
        return
    
    depth = [INF] * idx
    higher_island = [-1] * idx
    blocking_island = []
    
    for i in range(idx):
        visited = [[False]*m for _ in range(n)]
        blocking_island.append(get_blocking_island(sea,visited,island_list[i])) #영역 바깥으로 이동하는 것을 막는 섬의 목록을 구함
    
    while True:
        finish = True
        for i in range(idx):
            if depth[i] < INF: continue
            finish = False
            if blocking_island[i] == []:
                depth[i] = 0
            else:
                for parent_island in blocking_island[i]:
                    if depth[parent_island] + 1 < depth[i]:
                        higher_island[i] = parent_island
                        depth[i] = depth[parent_island] + 1                
        if finish == True:
            break
    
    answer = [0] * (max(depth) + 1)
    start = [True] * idx #높이가 0인 섬 목록
    
    for i in range(idx):
        if depth[i] == 0: continue
        start[higher_island[i]] = False
    
    visited = [False] * idx
    
    for i in range(idx):
        if start[i] == True:
            dfs(higher_island,visited,answer,i,0)
    
    for i in answer:
        print(i,end=" ")

def get_sea():
    sea = []
    for _ in range(n):
        sea.append(list(input()))
    return sea

def get_island_area(graph,start,idx):
    queue = deque([start])
    ret_value = [start]
    dx = [0,1,0,-1,-1,-1,1,1]
    dy = [1,0,-1,0,-1,1,-1,1]
    graph[start[0]][start[1]] = idx
    while queue:
        vx, vy = queue.popleft()
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if graph[nx][ny] == 'x':
                graph[nx][ny] = idx
                queue.append((nx,ny))
                ret_value.append((nx,ny))
    return ret_value

def get_blocking_island(graph,visited,start):
    ret_value = []
    queue = deque(start)
    original_idx = graph[start[0][0]][start[0][1]]
    dx_dy = [(0,1),(1,0),(-1,0),(0,-1)]
    for x,y in start:
        visited[x][y] = True
    while queue:
        vx,vy = queue.popleft()
        if vx == 0 or vy == 0 or vx == n-1 or vy == m-1:
            return []
        for dx,dy in dx_dy:
            nx = vx + dx
            ny = vy + dy
            if visited[nx][ny] == True or graph[nx][ny] == original_idx: continue
            visited[nx][ny] = True
            if graph[nx][ny] == '.':
                queue.append((nx,ny))
            else:
                ret_value.append(graph[nx][ny])
    return ret_value

def dfs(higher_island,visited,answer,vx,high):
    answer[high] += 1
    visited[vx] = True
    nx = higher_island[vx]
    if higher_island[vx] == -1 or visited[nx] == True: return
    dfs(higher_island,visited,answer,nx,high+1)

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()