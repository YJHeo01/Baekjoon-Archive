from collections import deque

def main():
    INF = int(1e9)
    graph = init_graph(n)
    visited = [[[[INF]*(2**m) for _ in range(2**n)]for _ in range(m)] for _ in range(n)]
    bfs(graph,visited)
    answer = INF
    for x in range(2**n):
        for y in range(2**m):
            answer = min(answer,visited[n-1][m-1][x][y])
    if answer >= INF: answer = -1
    print(answer)

def init_graph(n):
    graph = []
    for _ in range(n):
        graph.append(list(input()))
    return graph

def bfs(graph,visited):
    queue = deque([(0,0,0,0)])
    visited[0][0][0][0] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    possible_move = {
        'A':[[True,True,True,True],[True,True,True,True]],
        'C':[[False,False,True,True],[True,True,False,False]],
        'D':[[True,True,False,False],[False,False,True,True]]
        }
    while queue:
        vx,vy,row_button,column_button = queue.popleft()
        print(vx,vy)
        if graph[vx][vy] == 'B': continue
        state = 0
        if (2 ** vx) & row_button != 0: state += 1
        if (2 ** vy) & column_button != 0: state += 1
        if state == 2: state = 0
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if possible_move[graph[vx][vy]][state][i] == False: continue
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 'B': continue
            next_state = 0
            if (2 ** nx) & row_button != 0: next_state += 1
            if (2 ** ny) & column_button != 0: next_state += 1
            if next_state == 2: next_state = 0
            if possible_move[graph[nx][ny]][next_state][i] == False:continue
            if visited[nx][ny][row_button][column_button] > visited[vx][vy][row_button][column_button] + 1:
                visited[nx][ny][row_button][column_button] = visited[vx][vy][row_button][column_button] + 1
                queue.append((nx,ny,row_button,column_button))
        next_row_button = row_button
        if row_button & (2 ** vx) != 0: next_row_button - (2**vx)
        else: next_row_button += (2**vx)
        next_column_button = column_button
        if column_button & (2 ** vy) != 0: next_column_button - (2**vy)
        else: next_column_button += (2**vy)
        if visited[vx][vy][next_row_button][next_column_button] > visited[vx][vy][row_button][column_button] + 1:
            visited[vx][vy][next_row_button][next_column_button] = visited[vx][vy][row_button][column_button] + 1
            queue.append((vx,vy,next_row_button,next_column_button))
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()