import sys

sys.setrecursionlimit(500*500+1)

input = sys.stdin.readline

r,c = map(int,input().split())

board = []

for _ in range(r):
    board.append(list(map(int,input().split())))

result = [[-1]*c for _ in range(r)]

def solution(board,result,start):
    x,y = start
    if result[x][y] != -1:
        return result[x][y]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    nx, ny = start
    for i in range(8):
        if x + dx[i] < 0 or x + dx[i] >= r or y + dy[i] < 0 or y + dy[i] >= c: continue
        if board[nx][ny] > board[x+dx[i]][y+dy[i]]:
            nx = x + dx[i]
            ny = y + dy[i]
    result[x][y] = (x,y)
    if nx != x or ny != y:
        result[x][y] = solution(board,result,(nx,ny))
    return result[x][y]

for i in range(r):
    for j in range(c):
        if result[i][j] == -1:
            solution(board,result,(i,j))

answer = [[0]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        answer[result[i][j][0]][result[i][j][1]] += 1

for i in range(r):
    for j in range(c):
        print(answer[i][j],end=" ")
    print()