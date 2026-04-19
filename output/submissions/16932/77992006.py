from collections import deque
import sys

input = sys.stdin.readline

def main():
    array = get_array()
    visited = [[-1]*m for _ in range(n)]
    area_size_list = search_area(array,visited)
    answer = solution(visited,area_size_list)
    print(answer)

def get_array():
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    return array

def search_area(array,visited):
    area_idx = 0
    ret_value = []
    for x in range(n):
        for y in range(m):
            if array[x][y] == 0 or visited[x][y] != -1:
                continue
            visited[x][y] = area_idx
            size = bfs(array,visited,(x,y))
            ret_value.append(size)
            area_idx += 1
    return ret_value

def bfs(graph,visited,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    idx = visited[start[0]][start[1]]
    ret_value = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_array(nx,ny) or visited[nx][ny] == idx or graph[nx][ny] == 0:
                continue
            visited[nx][ny] = idx
            ret_value += 1
            queue.append((nx,ny))
    return ret_value

def exit_array(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    return False

def solution(visited,area_size_list):
    global area_cnt
    area_cnt = len(area_size_list)
    answer = 1
    for x in range(n):
        for y in range(m):
            if visited[x][y] != -1:
                continue  
            size = get_size(area_size_list,visited,(x,y))
            answer = max(answer,size)
    return answer

def get_size(area_size_list,visited,point):
    x,y = point
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 1
    meet_area = [False] * area_cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if exit_array(nx,ny) or visited[nx][ny] == -1: continue
        idx = visited[nx][ny]
        if meet_area[idx] == True:
            continue
        meet_area[idx] = True; ret_value += area_size_list[idx]
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()