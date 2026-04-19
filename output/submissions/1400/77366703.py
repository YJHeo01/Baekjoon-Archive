from collections import deque

INF = int(1e9)

def check_red_signal(state,cross_idx,direction_idx):
    if state[cross_idx] == '-':
        if direction_idx > 1:
            return True
    else:
        if direction_idx < 2:
            return True
    return False

def use_timer(timer,time_table,state):
    l = len(timer)
    for i in range(l):
        timer[i] -= 1
        if timer[i] == 0:
            if state[i] == '|':
                state[i] = '-'
                timer[i] = time_table[i][0]
            else:
                state[i] = '|'
                timer[i] = time_table[i][1]

def solution(graph,visited,start,timer,time_table,state):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    time = 0
    while queue:
        vx,vy = queue.popleft()
        if visited[vx][vy] != time:
            time = visited[vx][vy]
            use_timer(timer,time_table,state)
        red_signal = False
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == '.':
                continue
            if visited[nx][ny] > visited[vx][vy] + 1:
                if graph[nx][ny].isdigit() == True:
                    if check_red_signal(state,int(graph[nx][ny]),i) == True:
                        red_signal = True
                        continue
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))
        if red_signal == True:
            visited[vx][vy] += 1
            queue.append((vx,vy))

while True:
    m,n = map(int,input().split())
    graph = []; state = []; time_table = []; timer = []
    for _ in range(m):
        graph.append(list(input()))
    while True:
        try:
            cross_idx, cross_state, ai, bi = input().split()
            time_table.append([int(ai),int(bi)])
            state.append(cross_state)
            if cross_state == '|':
                timer.append(int(bi))
            else:
                timer.append(int(ai))
        except EOFError:
            break 
    if m == 0:
        break
    start = (-1,-1)
    end = (-1,-1)
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 'A':
                start = (i,j)
            elif graph[i][j] == 'B':
                end = (i,j)
    visited = [[INF]*n for _ in range(m)]
    solution(graph,visited,start,timer,time_table,state)
    answer = visited[end[0]][end[1]]
    if answer >= INF:
        answer = "impossible"
    print(answer)