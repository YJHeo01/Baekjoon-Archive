from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

def get_target(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'F':
                return (i,j)

board = [list(input().rstrip()) for _ in range(n)]
target = get_target(board)

def solution(board,visited,start):
    queue = deque([start])
    ret_value = 0
    visited[start[0]][start[1]] = True
    dx = [-1,-1,-1,0,0,1,1]
    dy = [-1,0,1,-1,1,-1,1]
    while queue:
        vx,vy = queue.popleft()
        for i in range(7):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if visited[nx][ny] == False and board[nx][ny] == '.':
                visited[nx][ny] = True
                ret_value += 1
                queue.append((nx,ny))
    return ret_value

print(solution(board,[[False]*n for _ in range(n)],target))