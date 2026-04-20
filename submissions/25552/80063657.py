from collections import deque
import sys

input = sys.stdin.readline

def main():
    init_grass = get_grass()
    d = int(input())
    result_grass = get_grass()
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if init_grass[i][j] == 'O' and visited[i][j] == False:
                visited[i][j] = True
                move_grass(result_grass,visited,(i,j),d)
    answer = 'YES'
    for i in range(n):
        for j in range(m):
            if (result_grass[i][j] == 'O' and visited[i][j] == False) or (result_grass[i][j] == 'X' and visited[i][j] == True):
                answer = 'NO'
                break
    print(answer)

def get_grass():
    grass = []
    for _ in range(n):
        grass.append(list(input()))
    return grass

def move_grass(result_grass,visited,start,d):
    queue = deque([start])
    direction = [(-1,-1),(1,1),(-1,1),(1,-1)]
    while queue:
        vx,vy = queue.popleft()
        for length in range(d+1):
            for move_x in range(length+1):
                move_y = length - move_x
                for i in range(4):
                    nx = vx + move_x * direction[i][0]
                    ny = vy + move_y * direction[i][1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if result_grass[nx][ny] == 'O' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx,ny))

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()