from collections import deque
import heapq

def main():
    maze = [list(input()) for _ in range(n)]
    node = get_node(maze,n)
    node.append(get_node(maze,n))
    INF = int(1e9)
    adj_matrix = [[INF]*(m+1) for _ in range(m+1)]
    for a in range(m+1):
        node_a = node[a]
        distance = [[-1]*n for _ in range(n)]
        set_edge_value(maze,distance,node_a)
        for b in range(m+1):
            b_x, b_y = node[b]
            if distance[b_x][b_y] == 0: continue
            if distance[b_x][b_y] < 0:
                print(-1)
                return
            adj_matrix[a][b] = distance[b_x][b_y]
    visited_node = [False] * (m+1)
    visited_edge = [[False] * (m+1) for _ in range(m+1)]
    answer = solution(adj_matrix,visited_node,visited_edge,[2]*(m+1))
    for i in range(m+1):
        if visited_edge[i] == False: answer = -1
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

def solution(graph,visited_node,visited_edge,cnt):
    ret_value = 0
    q = []
    cnt[0] = 1
    visited_node[0] = True
    for i in range(m+1):
        heapq.heappush(q,(graph[0][i],0,i))
    while q:
        dist, last_node, cur_node = heapq.heappop(q)
        if cnt[last_node] == 0 or visited_node[cur_node]: continue
        visited_node[cur_node] = True
        cnt[last_node] -= 1
        ret_value += dist
        for next_node in range(m+1):
            if visited_node[next_node] or visited_edge[cur_node][next_node]: continue
            visited_edge[cur_node][next_node] = True
            heapq.heappush(q,(graph[cur_node][next_node],cur_node,next_node))
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()