from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int,input().split())))

def crash_block_bfs(graph,visited,start):
    queue = deque([start])
    room_size = 1
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            if (graph[vx][vy] // (2**i)) % 2 == 1:
                continue
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            room_size += 1
            queue.append((nx,ny))
    return room_size

    

def non_crash_block_bfs(graph,original_room_visited,start):
    original_room_size = 1
    side_room_size = 0
    queue = deque([start])
    original_room_visited[start[0]][start[1]] = True
    side_room_visited = [[False]*n for _ in range(m)]
    side_room_visited[start[0]][start[1]] = True
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    crash_block_list = []
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if (graph[vx][vy] // (2**i)) % 2 == 0:
                if original_room_visited[nx][ny] == False:
                    original_room_visited[nx][ny] = True
                    side_room_visited[nx][ny] = True
                    original_room_size += 1
                    queue.append((nx,ny))
            else:
                crash_block_list.append((nx,ny))
    for point in crash_block_list:
        side_room_size = max(side_room_size,crash_block_bfs(graph,side_room_visited,point))
    return (original_room_size,original_room_size+side_room_size)


first_answer = 0
second_answer = 0
third_answer = 0
visited = [[False]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            first_answer += 1
            tmp_a, tmp_b = non_crash_block_bfs(graph,visited,(i,j))
            second_answer = max(second_answer,tmp_a)
            third_answer = max(third_answer,tmp_b)

print(first_answer)
print(second_answer)
print(third_answer)