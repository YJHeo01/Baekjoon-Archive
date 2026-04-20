import sys

input = sys.stdin.readline

r,c,n = map(int,input().split())

board = [[0]*c for _ in range(r)]

for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'O':
            board[i][j] = 4

def set_bomb(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                graph[i][j] = 4
            else:
                graph[i][j] -= 1

def explosion_bomb(graph):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 1:
                graph[x][y] = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == 1:
                        continue
                    graph[nx][ny] = 0

def print_answer(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                print(".",end="")
            else:
                print("O",end="")
        print()

def stop_bomberman(graph):
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0:
                graph[i][j] -= 1
    
def solution(graph,n):
    stop_bomberman(graph)
    for _ in range(n-1):
        set_bomb(graph)
        explosion_bomb(graph)
    print_answer(graph)    

solution(board,n)
