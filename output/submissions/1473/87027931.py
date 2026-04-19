import heapq

def main():
    maze = [list(input()) for _ in range(n)]
    distance = [[[[INF]*(1<<m) for _ in range(1<<n)] for _ in range(m)] for _ in range(n)]
    dijkstra(maze,distance)
    answer = INF
    for i in range(1<<n):
        for j in range(1<<m):
            answer = min(answer,distance[n-1][m-1][i][j])
    if answer >= INF: answer = -1
    print(answer)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,0,0,0,0))
    distance[0][0][0][0] = 0
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    possible = {'A':[[True,True,True,True],[True,True,True,True]],
                'B':[[False,False,False,False], [False, False, False, False]],
                'C':[[True,False,True,False],[False,True,False,True]],
                'D':[[False,True,False,True],[True,False,True,False]]    
                }
    while q:
        dist, vx, vy, row_bit, column_bit = heapq.heappop(q)
        if dist > distance[vx][vy][row_bit][column_bit]: continue
        cur_state = 0
        if (1 << vx) & row_bit: cur_state += 1
        if (1 << vy) & column_bit: cur_state += 1
        cur_state %= 2
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or possible[graph[vx][vy]][cur_state][i] == False: continue
            next_state = 0
            if (1<<nx) & row_bit:next_state += 1
            if (1<<ny) & column_bit: next_state += 1
            next_state %= 2
            if possible[graph[nx][ny]][next_state][i] == False or dist + 1 >= distance[nx][ny][row_bit][column_bit]: continue
            distance[nx][ny][row_bit][column_bit] = dist + 1
            heapq.heappush(q,(dist+1,nx,ny,row_bit,column_bit))
        next_row_bit = row_bit
        next_column_bit = column_bit
        if (1<<vx) & next_row_bit: next_row_bit -= (1<<vx)
        else: next_row_bit |= (1<<vx)
        if (1<<vy) & next_column_bit: next_column_bit -= (1<<vy)
        else: next_column_bit |= (1<<vy)
        if distance[vx][vy][next_row_bit][next_column_bit] > dist + 1:
            distance[vx][vy][next_row_bit][next_column_bit] = dist + 1
            heapq.heappush(q,(dist+1,vx,vy,next_row_bit,next_column_bit))

if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()