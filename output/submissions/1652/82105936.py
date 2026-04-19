def main():
    row_visited = [[False]*n for _ in range(n)]
    column_visited = [[False]*n for _ in range(n)]
    room = [list(input()) for _ in range(n)]
    row_answer, column_answer = 0,0
    for i in range(n):
        for j in range(n):
            if room[i][j] == 'X':
                continue
            if row_visited[i][j] == False:
                row_answer += sleep_row(room,row_visited,(i,j))
            if column_visited[i][j] == False:
                column_answer += sleep_column(room,column_visited,(i,j))
    print(row_answer,column_answer)

def sleep_row(room,visited,start):
    x,y = start
    visited[x][y] = True
    cnt = 1
    while True:
        y += 1
        if y >= n or room[x][y] == 'X':
            break
        visited[x][y] = True
        cnt += 1
    if cnt >= 2:
        return 1
    return 0

def sleep_column(room,visited,start):
    x,y = start
    visited[x][y] = True
    cnt = 1
    while True:
        x += 1
        if x >= n or room[x][y] == 'X':
            break
        visited[x][y] = True
        cnt += 1
    if cnt >= 2:
        return 1
    return 0

if __name__ == "__main__":
    n = int(input())
    main()