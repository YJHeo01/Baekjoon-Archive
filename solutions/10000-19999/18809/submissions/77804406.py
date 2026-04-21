from itertools import combinations
INF = int(1e9)

def main():
    garden = get_garden()
    start_point = get_start_point(garden)
    green_start_list = list(combinations(start_point,g))
    answer = 0
    for green_start in green_start_list:
        data = get_data(start_point,green_start)
        red_start_list = list(combinations(data,r))
        for red_start in red_start_list:
            answer = max(answer,solution(garden,list(green_start),list(red_start)))
    print(answer)

def get_garden():
    garden = []
    for _ in range(n):
        garden.append(list(map(int,input().split())))
    return garden

def get_start_point(graph):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                ret_value.append((i,j))
    return ret_value

def get_data(start_point,green_start):
    data = []
    for i in start_point:
        if i in green_start:
            continue
        data.append(i)
    return data

def solution(graph,green,red):
    green_visited = [[INF]*m for _ in range(n)]
    red_visited = [[INF]*m for _ in range(n)]
    init_visited(green_visited,green); init_visited(red_visited,red)
    while green and red:
        green = move_green(graph,red_visited,green_visited,green)
        red = move_red(graph,red_visited,green_visited,red)
    flower_cnt = get_flower_cnt(red_visited,green_visited)
    return flower_cnt

def init_visited(visited,color):
    for x,y in color:
        visited[x][y] = 0
    return visited

def move_green(graph,red_visited,green_visited,green):
    ret_value = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while green:
        vx,vy = green.pop()
        if red_visited[vx][vy] == green_visited[vx][vy]:
            continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_garden(nx,ny) == True or graph[nx][ny] == 0:
                continue
            if green_visited[nx][ny] > green_visited[vx][vy] + 1 :
                green_visited[nx][ny] = green_visited[vx][vy] + 1
                if green_visited[nx][ny] >= red_visited[nx][ny]:
                    continue    
                ret_value.append((nx,ny))
    return ret_value

def exit_garden(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    return False

def move_red(graph,red_visited,green_visited,red):
    ret_value = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while red:
        vx, vy = red.pop()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_garden(nx,ny) or graph[nx][ny] == 0:
                continue
            if red_visited[nx][ny] > red_visited[vx][vy] + 1:
                red_visited[nx][ny] = red_visited[vx][vy] + 1                
                if red_visited[nx][ny] >= green_visited[nx][ny]:
                    continue
                ret_value.append((nx,ny))
    return ret_value
 
def get_flower_cnt(red,green):
    ret_value = 0
    for i in range(n):
        for j in range(m):
            if red[i][j] == INF:
                continue
            if red[i][j] == green[i][j]:
                ret_value += 1
    return ret_value

if __name__ == "__main__":
    n,m,g,r = map(int,input().split())
    main()