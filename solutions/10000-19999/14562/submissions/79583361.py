from collections import deque

def main():
    c = int(input())
    for _ in range(c):
        s,t = map(int,input().split())
        global max_value
        max_value = t + (t-s) * 3
        visited = [[max_value]*(max_value+1) for _ in range(max_value+1)]
        bfs(visited,(s,t))
        answer = max_value
        for i in range(1,max_value+1):
            answer = min(answer,visited[i][i])
        print(answer)

def bfs(visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [1,0]
    dy = [0,3]
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if i == 1: nx *= 2
            if nx > max_value or ny > max_value:continue
            if visited[nx][ny] == max_value:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    main()