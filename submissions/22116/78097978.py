from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    board = get_board()
    visited = [[INF]*n for _ in range(n)]
    answer = solution(board,visited)
    print(answer)

def get_board():
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    return board

def solution(graph,visited):
    queue = deque([(0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[0][0] = 0 
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] > max(visited[vx][vy],abs(graph[nx][ny]-graph[vx][vy])):
                visited[nx][ny] = max(visited[vx][vy],abs(graph[nx][ny]-graph[vx][vy]))
                queue.append((nx,ny))
    return visited[n-1][n-1]

if __name__ == "__main__":
    n = int(input())
    main()