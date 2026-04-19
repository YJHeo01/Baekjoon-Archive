from collections import deque
import sys

input = sys.stdin.readline

def main():
    array = [list(map(int,input().split())) for _ in range(5)]
    r,c = map(int,input().split())
    max_state = 1 << 6
    visited = [[[INF]*5 for _ in range(5)] for _ in range(max_state)]
    bfs(array,visited,(0,r,c))
    answer = INF
    for i in range(5):
        for j in range(5):
            answer = min(answer,visited[max_state-1][i][j])
    if answer >= INF: answer = -1
    print(answer)

def bfs(graph,visited,start):
    
    queue = deque([start])
    visited[0][start[1]][start[2]] = 0
    while queue:
        vb,vx,vy = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = vx+dx,vy+dy
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == -1: continue
            nb = vb
            if graph[nx][ny] != 0 and graph[nx][ny] != 7:
                nb |= 1 << (graph[nx][ny]-1)
            if visited[nb][nx][ny] > visited[vb][vx][vy] + 1:
                visited[nb][nx][ny] = visited[vb][vx][vy] + 1
                queue.append((nb,nx,ny))
            nx,ny = run(graph,(nx,ny),dx,dy)
            
            #print(vx,vy,nx,ny)
            nb = vb
                
            if graph[nx][ny] > 0 and graph[nx][ny] != 7:
                nb |= 1 << (graph[nx][ny]-1)
            #print(visited[nb][nx][ny],visited[vb][vx][vy])
            if visited[nb][nx][ny] > visited[vb][vx][vy] + 1:
                visited[nb][nx][ny] = visited[vb][vx][vy] + 1
                queue.append((nb,nx,ny))

def run(graph,pos,dx,dy):
    x,y = pos
    while True:

        if x < 0 or y < 0 or x >= 5 or y >= 5 or graph[x][y] == -1:
            x -= dx
            y -= dy
            break
        if graph[x][y] == 7: break
        x += dx
        y += dy

    return x,y
        
if __name__ == "__main__":
    INF = int(1e9)
    main()