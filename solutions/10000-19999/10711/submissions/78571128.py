from collections import deque

INF = int(1e9)

def main():
    graph = get_graph(h)
    visited = [[0]*w for _ in range(h)]
    answer = solution(graph,visited)
    print(answer)

def get_graph(h):
    graph = []
    for _ in range(h): graph.append(list(input()))
    return graph

def solution(graph,visited):
    queue = init_queue(graph,visited)
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    ret_value = 0
    while queue:
        vx,vy = queue.popleft()
        ret_value = visited[vx][vy]
        for i in range(8):
            nx = vx + dx[i]; ny = vy + dy[i]
            if exit_graph(nx,ny) or visited[nx][ny] != INF: continue
            if graph[nx][ny] == '.' or graph[nx][ny] == 9: continue
            cnt = 0
            for k in range(8):
                x = nx + dx[k]; y = ny + dy[k]
                if exit_graph(x,y) : continue
                if ret_value >= visited[x][y]: cnt += 1
            if graph[nx][ny] > cnt:continue
            visited[nx][ny] = visited[vx][vy] + 1
            queue.append((nx,ny))
    return ret_value

def init_queue(graph,visited):
    queue = deque([])
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    for x in range(h):
        for y in range(w):
            if graph[x][y] == '.': continue
            graph[x][y] = int(graph[x][y])
            cnt = 0
            for k in range(8):
                nx = x + dx[k]; ny = y + dy[k]
                if exit_graph(nx,ny): continue
                if graph[nx][ny] == '.': cnt += 1
            if graph[x][y] > cnt:visited[x][y] = INF
            else: 
                visited[x][y] = 1
                queue.append((x,y))
    return queue

def exit_graph(x,y):
    if x < 0 or y < 0 or x >= h or y >= w: return True
    return False

if __name__ == "__main__":
    h,w = map(int,input().split())
    main()