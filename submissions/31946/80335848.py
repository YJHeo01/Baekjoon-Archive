from collections import deque
import sys

input = sys.stdin.readline

def main():
    block = []
    for _ in range(n):
        block.append(list(map(int,input().split())))
    if block[0][0] != block[n-1][m-1]:
        print("DEAD")
        return
    visited = [[False]*m for _ in range(n)]
    bfs(block,visited,int(input()))
    if visited[n-1][m-1]: print("ALIVE")
    else: print("DEAD")

def bfs(graph,visited,max_distance):
    queue = deque([(0,0)])
    visited[0][0] = True
    multiple_dx = [-1,-1,1,1]
    multiple_dy = [-1,1,-1,1]
    while queue:
        vx,vy = queue.popleft()
        for move_distance in range(1,max_distance+1):
            for dx in range(move_distance+1):
                dy = move_distance - dx
                for i in range(4):
                    nx = vx + dx * multiple_dx[i]
                    ny = vy + dy * multiple_dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] != graph[0][0]: continue
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    main()