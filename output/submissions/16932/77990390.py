from collections import deque
import sys

input = sys.stdin.readline

def main():
    array = get_array()
    answer = solution(array)
    print(answer)

def get_array():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    return array

def solution(array):
    answer = 0; visit_idx = 0
    visited = [[-1]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if array[x][y] == 1:
                continue
            adj_area = get_adj_area(array,(x,y))
            if check_duplication(visited,adj_area,visit_idx): continue
            visit_idx += 1; visited[x][y] = visit_idx
            answer = max(answer,bfs(array,visited,(x,y)))
    return answer

def get_adj_area(array,point):
    ret_value = []
    x,y = point
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if check_exit(nx,ny) or array[nx][ny] == 0: continue
        ret_value.append((nx,ny))
    return ret_value

def check_exit(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    return False

def check_duplication(visited,start,idx):
    for x,y in start:
        if visited[x][y] != idx:
            return False
    return True

def bfs(graph,visited,start):
    queue = deque([start])
    idx = visited[start[0]][start[1]]
    ret_value = 1
    dx = [0,1,0,-1]; dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if check_exit(nx,ny) or visited[nx][ny] == idx or graph[nx][ny] == 0:
                continue
            visited[nx][ny] = idx
            queue.append((nx,ny))
            ret_value += 1
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()