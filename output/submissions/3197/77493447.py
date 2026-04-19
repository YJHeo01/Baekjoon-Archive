from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    lake = get_lake()
    melt_time = [[0]*c for _ in range(r)]
    visited = [[INF]*c for _ in range(r)]
    edge = get_edge(lake,melt_time)
    start,end = get_start_end(lake)
    init_melt_time(melt_time,edge)
    solution(melt_time,visited,start)
    answer = visited[end[0]][end[1]]
    print(answer)

def get_lake():
    lake = []
    for _ in range(r):
        lake.append(list(input()))
    return lake

def get_edge(lake,melt_time):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = []
    for x in range(r):
        for y in range(c):
            if lake[x][y] == 'X':
                melt_time[x][y] = INF
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if exit_lake(nx,ny):
                    continue
                if lake[nx][ny] == 'X':
                    ret_value.append((x,y))
                    break
    return ret_value

def exit_lake(x,y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return True
    return False

def get_start_end(lake):
    start = (-1,-1)
    for i in range(r):
        for j in range(c):
            if lake[i][j] == 'L':
                if start == (-1,-1):
                    start = (i,j)
                else:
                    end = (i,j)
                    return start,end
    return start,end

def init_melt_time(melt_time,edge):
    queue = deque(edge)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_lake(nx,ny):
                continue
            if melt_time[nx][ny] > melt_time[vx][vy] + 1:
                melt_time[nx][ny] = melt_time[vx][vy] + 1
                queue.append((nx,ny))
    
def solution(melt_time,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_lake(nx,ny):
                continue
            if visited[nx][ny] > max(visited[vx][vy],melt_time[nx][ny]):
                visited[nx][ny] = max(visited[vx][vy],melt_time[nx][ny])
                queue.append((nx,ny))

if __name__ == "__main__":
    r,c = map(int,input().split())
    main()