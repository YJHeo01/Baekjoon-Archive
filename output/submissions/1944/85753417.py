from collections import deque

def main():
    maze = [list(input()) for _ in range(n)]
    node = get_node(maze,n)
    node.append(get_node(maze,n))
    graph = [[] for _ in range(n+1)]
    for a in range(m+1):
        node_a = node[a]
        distance = [[-1]*n for _ in range(n)]
        set_edge_value(maze,distance,node_a)
        for b in range(m+1):
            if a == b: continue
            b_x, b_y = node[b]
            graph[a].append((distance[b_x][b_y],b))
        graph[a].sort()
    visited = [False] * (m+1)
    answer = solution(graph,visited)
    for i in range(m+1):
        if visited[i] == False: answer = -1
    print(answer)

def get_node(graph,n):
    node = [get_start(graph,n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'K':
                node.append((i,j))
    return node

def get_start(graph,n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'S': return (i,j)
    return (-1,-1)

def set_edge_value(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = 0
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == '1': continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[vx][vy] + 1
                queue.append((nx,ny))

def solution(graph,visited):
    ret_value = 0
    queue = deque([0])
    visited[0] = True
    while queue:
        vx = queue.popleft()
        cnt = 2
        for move_cnt, nx in graph[vx]:
            if visited[nx] == True: continue
            visited[nx] = True
            ret_value += move_cnt; cnt -= 1
            queue.append(nx)
            if cnt == 0: break
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()