from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

answer = 2

area_size_list = [0,0]

new_area_idx = 2

def get_new_area(array,start,idx):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ret_value = 1
    array[start[0]][start[1]] = idx
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 1:
                array[nx][ny] = idx
                ret_value += 1
                queue.append((nx,ny))
    return ret_value

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            new_area_size = get_new_area(array,(i,j),new_area_idx)
            answer = max(answer,new_area_size+1)
            new_area_idx += 1
            area_size_list.append(new_area_size)

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            tmp = 1
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            area_list = [False] * new_area_idx
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                area_idx = array[x][y]
                if area_list[area_idx] == False:
                    area_list[area_idx] = True
                    tmp += area_size_list[area_idx]
            answer = max(answer,tmp)

print(answer)