def main():
    r,c = map(int,input().split())
    graph = [list(input()) for _ in range(r)]
    
    adj_sea_cnt = [[0]* c for _ in range(r)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for vx in range(r):
        for vy in range(c):
            if graph[vx][vy] == '.': continue
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == '.': adj_sea_cnt[vx][vy] += 1
    
    min_x, max_x, min_y, max_y = r,0,c,0
    
    for vx in range(r):
        for vy in range(c):
            if adj_sea_cnt[vx][vy] >= 3: graph[vx][vy] = '.'
            if graph[vx][vy] == 'X':
                min_x = min(vx,min_x)
                max_x = max(vx,max_x)
                min_y = min(vy,min_y)
                max_y = max(vy,max_y)
    
    for x in range(min_x,max_x+1):
        for y in range(min_y,max_y+1):
            print(graph[x][y],end="")
        print()
    

if __name__ == "__main__":
    main()