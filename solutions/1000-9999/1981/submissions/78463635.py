from collections import deque

def main():
    matrix = get_matrix()
    answer = solution(matrix)
    print(answer)

def get_matrix():
    matrix = []
    for _ in range(n): matrix.append(list(map(int,input().split())))
    return matrix

def solution(matrix):
    left, right = 0,200
    ret_value = 200
    first_value = matrix[0][0]
    while left <= right:
        limit = (left + right) // 2
        visited = get_init_visited(first_value)
        bfs(matrix,visited,limit)
        if check_correct_limit(visited[n-1][n-1]) == True:
            ret_value = limit
            right = limit - 1
        else: left = limit + 1
    return ret_value

def get_init_visited(first_value):
    visited = [[[[False]*(first_value+1) for _ in range(200-first_value+1)]for _ in range(n)]for _ in range(n)]
    for i in range(first_value+1):
        for j in range(200-first_value+1):
            visited[0][0][j][i] = True
    return visited

def bfs(graph,visited,limit):
    queue = deque([(0,0,0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    first_value = graph[0][0]
    while queue:
        vx,vy,cur_max,cur_min= queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >=n: continue
            next_max = max(cur_max,graph[nx][ny]- first_value)
            next_min = max(cur_min,first_value - graph[nx][ny])
            if visited[nx][ny][next_max][next_min] == True or next_max + next_min > limit: continue
            visited[nx][ny][next_max][next_min] = True
            queue.append((nx,ny,next_max,next_min))

def check_correct_limit(visited):
    for row in visited:
        for value in row:
            if value == True:
                return True
    return False

if __name__ == "__main__":
    n = int(input())
    main()