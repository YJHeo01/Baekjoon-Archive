from collections import deque
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

INF = int(1e9)

def main():
    case_idx = 0
    while True:
        try:
            case_idx += 1
            global n,m
            n,m = map(int,input().split())
            board = []
            for _ in range(n):
                board.append(list(input()))
            answer = INF
            for i in range(n):
                for j in range(m):
                    if board[i][j] == '*':
                        continue
                    visited = get_init_visited(board)
                    answer = min(answer,solution(visited,(i,j),1))
            if answer >= INF:
                answer = -1
            print("Case " + str(case_idx) + ": " + str(answer))
        except EOFError:
            break

def get_init_visited(board):
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                visited[i][j] = True
    return visited
    
def solution(visited,start,move_cnt):
    ret_value = INF
    x,y = start
    if x > 0 and visited[x-1][y] == False:
        new_visited = get_new_visited(visited)
        new_start = move_ball(new_visited,start,(-1,0))
        if game_over(new_visited) == True:
            return move_cnt
        ret_value = min(ret_value,solution(new_visited,new_start,move_cnt+1))

    if y > 0 and visited[x][y-1] == False:
        new_visited = get_new_visited(visited)
        new_start = move_ball(new_visited,start,(0,-1))
        if game_over(new_visited) == True:
            return move_cnt
        ret_value = min(ret_value,solution(new_visited,new_start,move_cnt+1))

    if x < n-1 and visited[x+1][y] == False:
        new_visited = get_new_visited(visited)
        new_start = move_ball(new_visited,start,(1,0))
        if game_over(new_visited) == True:
            return move_cnt
        ret_value = min(ret_value,solution(new_visited,new_start,move_cnt+1))
    
    if y < m-1 and visited[x][y+1] == False:
        new_visited = get_new_visited(visited)
        new_start = move_ball(new_visited,start,(0,1))
        if game_over(new_visited) == True:
            return move_cnt
        ret_value = min(ret_value,solution(new_visited,new_start,move_cnt+1))
    return ret_value

def get_new_visited(visited):
    ret_value = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ret_value[i][j] = visited[i][j]
    return ret_value

def move_ball(visited,start,direction):
    dx,dy = direction
    x,y = start
    while True:
        visited[x][y] = True
        nx = x + dx; ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] == True:
            return x,y
        x = nx; y = ny

def game_over(visited):
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                return False
    return True

if __name__ == "__main__":
    main()