from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

ascii_A = ord('A')
ascii_Z = ord('Z')
ascii_a = ord('a')
ascii_z = ord('z')
def bfs(graph,visited,start,key_list,door):
    ret_value = 0
    queue = deque(start)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >=w:
                continue
            if visited[nx][ny] == False and graph[nx][ny] != '*':
                visited[nx][ny] = True
                ascii_point = ord(graph[nx][ny])
                if graph[nx][ny] == '$':
                    ret_value += 1
                    queue.append((nx,ny))
                elif ascii_A <= ascii_point and ascii_point <= ascii_Z:
                    idx = ascii_point - ascii_A
                    if key_list[idx] == True:
                        queue.append((nx,ny))
                    else:
                        door[idx].append((nx,ny))
                elif ascii_a <= ascii_point and ascii_point <= ascii_z:
                    idx = ascii_point - ascii_a
                    queue.append((nx,ny))
                    key_list[idx] = True
                    if door[idx] != []:
                        queue = queue + deque(door[idx])
                else:
                    queue.append((nx,ny))
    return ret_value
                        
#가장자리에 문서가 있는 경우를 추가해야
for _ in range(t):
    answer = 0
    h,w = map(int,input().split())
    visited = [[False]*w for _ in range(h)]
    building = []
    for _ in range(h):
        building.append(list(input()))
    get_key = [False] * 26
    start = []
    door = [[] for _ in range(26)]

    for i in range(w):
        visited[0][i], visited[h-1][i] = True, True
        if building[0][i] != '*':
            ascii_point = ord(building[0][i])
            if ascii_A <= ascii_point and ascii_point <= ascii_Z:
                idx = ascii_point - ascii_A
                if get_key[idx] == True:
                    start.append((0,i))
                else:
                    door[idx].append((0,i))
            else:
                start.append((0,i))
                if building[0][i] != '.':
                    if building[0][i] == '$':
                        answer += 1
                    else:
                        idx = ascii_point - ascii_a
                        get_key[idx] = True

        if building[h-1][i] != '*':
            ascii_point = ord(building[h-1][i])
            if ascii_A <= ascii_point and ascii_point <= ascii_Z:
                idx = ascii_point - ascii_A
                if get_key[idx] == True:
                    start.append((h-1,i))
                else:
                    door[idx].append((h-1,i))
            else: 
                start.append((h-1,i))
                if building[h-1][i] != '.':
                    if building[h-1][i] == '$':
                        answer += 1
                    else:
                        idx = ascii_point - ascii_a
                        get_key[idx] = True
    
    for i in range(1,h-1):
        visited[i][0], visited[i][w-1] = True,True
        if building[i][0] != '*':
            ascii_point = ord(building[i][0])
            if ascii_A <= ascii_point and ascii_point <= ascii_Z:
                idx = ascii_point - ascii_A
                if get_key[idx] == True:
                    start.append((i,0))
                else:
                    door[idx].append((i,0))
            else:
                start.append((i,0))
                if building[i][0] != '.':
                    if building[i][0] == '$':
                        answer += 1
                    else:
                        idx = ascii_point - ascii_a
                        get_key[idx] = True
        
        if building[i][w-1] != '*':
            ascii_point = ord(building[i][w-1])
            if ascii_A <= ascii_point and ascii_point <= ascii_Z:
                idx = ascii_point - ascii_A
                if get_key[idx] == True:
                    start.append((i,w-1))
                else:
                    door[idx].append((i,w-1))
            else:
                start.append((i,w-1))
                if building[i][w-1] != '.':
                    if building[i][w-1] == '$':
                        answer += 1
                    else:
                        idx = ascii_point - ascii_a
                        get_key[idx] = True
    key_list = list(input().rstrip())
    if key_list[0] != '0':
        for key in key_list:
            idx = ord(key) - ascii_a
            get_key[idx] = True
            if door[idx] != []:
                start = start + door[idx]
                door[idx] = []
    answer += bfs(building,visited,start,get_key,door)
    print(answer)
    