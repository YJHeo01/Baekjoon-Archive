from collections import deque

INF = int(1e9)

def main():
    town_map = get_town_map()
    start = get_start(town_map)
    town_high = get_town_high()
    target = get_target(town_map)
    max_high_list = [[INF]*n for _ in range(n)]
    min_high_list = [[0]*n for _ in range(n)]
    bfs(town_high,max_high_list,min_high_list,start)
    max_high, min_high = town_high[start[0]][start[1]], town_high[start[0]][start[1]]
    for x,y in target:
        max_high = max(max_high,max_high_list[x][y])
        min_high = min(min_high,min_high_list[x][y])
    answer = max_high - min_high
    print(answer)

def get_town_map():
    town = []
    for _ in range(n):
        town.append(list(input()))
    return town

def get_town_high():
    high = []
    for _ in range(n):
        high.append(list(map(int,input().split())))
    return high

def get_start(town):
    for x in range(n):
        for y in range(n):
            if town[x][y] == 'P':
                return (x,y)

def get_target(town):
    ret_value = []
    for x in range(n):
        for y in range(n):
            if town[x][y] == 'K':
                ret_value.append((x,y))
    return ret_value

def bfs(graph,max_high,min_high,start):
    x,y = start
    max_high[x][y], min_high[x][y] = graph[x][y], graph[x][y]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    queue = deque([start])
    while queue:
        vx,vy = queue.popleft()
        cur_max_high, cur_min_high = max_high[vx][vy], min_high[vx][vy]
        for i in range(8):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            next_max_high = max(graph[nx][ny],cur_max_high)
            next_min_high = min(graph[nx][ny],cur_min_high)
            if max_high[nx][ny] - min_high[nx][ny] > next_max_high - next_min_high:
                max_high[nx][ny] = next_max_high; min_high[nx][ny] = next_min_high
                queue.append((nx,ny))
    
if __name__ == "__main__":
    n = int(input())
    main()