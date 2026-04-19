from collections import deque

def main():
    graph = get_graph()
    first_answer, second_answer, third_answer = 0,0,0
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                first_answer += 1
                room_size, crash_block_size = bfs(graph,visited,(i,j))
                second_answer = max(second_answer,room_size)
                third_answer = max(third_answer,crash_block_size)
    print(first_answer)
    print(second_answer)
    print(third_answer)

def get_graph():
    graph = []
    for _ in range(m):
        graph.append(list(map(int,input().split())))
    return graph

def bfs(graph,visited,start):
    room_size = 1; side_room_size = 0
    queue = deque([start])
    visited[start[0]][start[1]] = True
    after_crash_visited = [[False]*n for _ in range(m)]
    after_crash_visited[start[0]][start[1]] = True
    dx = [0,-1,0,1]; dy = [-1,0,1,0]
    crash_block_list = []
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_castle(nx,ny) or visited[nx][ny] == True: continue
            if (graph[vx][vy] // (2**i)) % 2 != 0:
                crash_block_list.append((nx,ny))
                continue
            visited[nx][ny] = True
            after_crash_visited[nx][ny] = True
            room_size += 1
            queue.append((nx,ny))            
    for point in crash_block_list:
        side_room_size = max(side_room_size,crash_block_bfs(graph,after_crash_visited,point))
    return (room_size,room_size+side_room_size)

def exit_castle(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return True
    return False

def crash_block_bfs(graph,visited,start):
    queue = deque([start])
    room_size = 1
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            if (graph[vx][vy] // (2**i)) % 2 == 1: continue
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_castle(nx,ny) or visited[nx][ny] == True: continue
            visited[nx][ny] = True; room_size += 1
            queue.append((nx,ny))
    return room_size

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()