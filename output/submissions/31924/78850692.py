import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())

board = []

for _ in range(n):
    board.append(list(input()))

answer = 0

def dfs(board,start,idx,d):
    x,y = start
    ret_value = 0
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    s = ['O','B','I','S']
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return 0
    if board[nx][ny] == s[idx]:
        if idx == 3:
            ret_value += 1
        else:
            ret_value += dfs(board,(nx,ny),idx+1,d)
    return ret_value

for x in range(n):
    for y in range(n):
        if board[x][y] == 'M':
            for d in range(8):
                answer += dfs(board,(x,y),0,d)
            
print(answer)