import sys

input = sys.stdin.readline

t = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(t):
    array = []
    n = int(input())
    for _ in range(2):
        tmp = list(map(int,input().split()))
        array.append(tmp)
    visited = [[0] * n for _ in range(2)]
    answer = 0
    visited_cnt = 0
    while 1:
        max_v = 0
        max_i = (0,0)
        for i in range(2):
            for j in range(n):
                if visited[i][j] == 1:
                    continue
                if array[i][j] > max_v:
                    max_v = array[i][j]
                    max_i = (i,j)
                elif array[i][j] == max_v:
                    new_edge = 0
                    max_edge = 0
                    for k in range(4):
                        nx = max_i[0] + dx[k]
                        ny = max_i[1] + dy[k]
                        new_x = i + dx[k]
                        new_y = j + dy[k]
                        if nx >= 0 and ny >= 0 and nx < 2 and ny < n and visited[nx][ny] == 0:
                            max_edge += array[nx][ny]
                        if new_x >= 0 and new_y >= 0 and new_x < 2 and new_y < n and visited[new_x][new_y] == 0:
                            new_edge += array[new_x][new_y]
                    if max_edge > new_edge:
                        max_i = (i,j)
        answer += max_v
        visited[max_i[0]][max_i[1]] = 1
        visited_cnt += 1
        for i in range(4):
            nx = max_i[0] + dx[i]
            ny = max_i[1] + dy[i]
            if nx < 0 or ny <0 or nx >= 2 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                visited_cnt += 1
        if visited_cnt >= 2*n:
            print(answer)
            break
