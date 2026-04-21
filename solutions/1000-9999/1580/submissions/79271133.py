from collections import deque

def main():
    graph = get_graph(n)
    a_position = get_position(graph,'A')
    b_position = get_position(graph,'B')
    INF = int(1e9)
    visited = [[[[INF]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
    bfs(graph,visited,a_position,b_position)
    A_x,A_y = a_position
    B_x,B_y = b_position
    answer = visited[B_x][B_y][A_x][A_y]
    if answer >= INF: answer = -1
    print(answer)

def get_graph(n):
    graph = []
    for _ in range(n):
        graph.append(list(input()))
    return graph

def get_position(graph,c):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == c:return(i,j)

def bfs(graph,visited,start_A,start_B):
    queue = deque([(start_A,start_B)])
    dx = [0,1,0,-1,1,1,-1,-1,0]
    dy = [1,0,-1,0,1,-1,1,-1,0]
    visited[start_A[0]][start_A[1]][start_B[0]][start_B[1]] = 0
    while queue:
        point_A, point_B = queue.popleft()
        A_vx, A_vy = point_A
        for i in range(9):
            A_nx = A_vx + dx[i]
            A_ny = A_vy + dy[i]
            if exit_board(A_nx,A_ny) or graph[A_nx][A_ny] == 'X':
                continue
            B_vx, B_vy = point_B
            for j in range(9):
                B_nx = B_vx + dx[j]
                B_ny = B_vy + dy[j]
                if exit_board(B_nx,B_ny) or graph[B_nx][B_ny] == 'X' or ((A_nx == B_nx) and (A_ny == B_ny)):
                    continue
                if ((B_nx,B_ny) == point_A and (A_nx,A_ny) == point_B) : continue
                if visited[A_nx][A_ny][B_nx][B_ny] > visited[A_vx][A_vy][B_vx][B_vy] + 1:
                    visited[A_nx][A_ny][B_nx][B_ny] = visited[A_vx][A_vy][B_vx][B_vy] + 1
                    queue.append(((A_nx,A_ny),(B_nx,B_ny)))
            
def exit_board(x,y):
    if x < 0 or y < 0 or x >= n or y >=m:return True
    return False

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()