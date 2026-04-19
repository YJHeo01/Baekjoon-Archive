from collections import deque

INF = int(1e9)

def main():
    matrix = get_matrix()
    visited = [[INF]*n for _ in range(n)]
    solution(matrix,visited)
    answer = visited[n-1][n-1]
    print(answer)

def get_matrix():
    matrix = []
    for _ in range(n): matrix.append(list(map(int,input().split())))
    return matrix

def solution(graph,visited):
    queue = deque([(0,0,graph[0][0],graph[0][0])])
    visited[0][0] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,cur_max,cur_min= queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >=n: continue
            next_max = max(cur_max,graph[nx][ny])
            next_min = min(cur_min,graph[nx][ny])
            if visited[nx][ny] > next_max - next_min:
                visited[nx][ny] = next_max - next_min
                queue.append((nx,ny,next_max,next_min))
            elif visited[nx][ny] == next_max - next_min:
                if next_max == cur_max and next_min == cur_min: continue
                queue.append((nx,ny,next_max,next_min))

if __name__ == "__main__":
    n = int(input())
    main()