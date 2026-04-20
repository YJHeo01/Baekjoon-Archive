answer = 0

def backtracking(graph,n,queen_list,point_list):
    global answer
    if len(queen_list) == n:
        dx = [1,1,0,-1,-1,-1,0,1]
        dy = [0,1,1,1,0,-1,-1,-1]
        tmp = []
        for queen in queen_list:
            x = queen // n
            y = queen % n
            tmp.append((x,y))
            graph[x][y] = 1
        for queen in tmp:
            x,y = queen
            for i in range(8):
                while 1:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        break
                    if graph[nx][ny] != 0:
                        for i in tmp:
                            graph[i[0]][i[1]] = 0
                        return
        for i in tmp:
            graph[i[0]][i[1]] = 0
        answer += 1
        return
    for point in point_list:
        if point not in queen_list:
            queen_list.append(point)
            backtracking(graph,n,queen_list,point_list)
            queen_list.pop()
    return
    


n = int(input())

chess = [[0] * n for _ in range(n)]

size = n**2

point_list = [0] * (size)

for i in range(size):
    point_list[i] = i

backtracking(chess,n,[],point_list)

print(answer)
