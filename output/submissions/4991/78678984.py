from collections import deque
import sys

input = sys.stdin.readline

def main():
    global h,w
    while True:
        w,h = map(int,input().split())
        if h == 0:break
        answer = solution()
        print(answer)
    
def solution():
    room = get_room(h)
    start = get_start(room)
    change_state = [[0]*w for _ in range(h)]
    trash_list = get_trash_list(room,change_state)
    trash_cnt = len(trash_list)
    if trash_cnt == 0: return 0
    z_size = 2 ** trash_cnt
    visited = [[[INF]*z_size for _ in range(w)]for _ in range(h)]
    visited[start[0]][start[1]][0] = 0
    bfs(room,visited,change_state,start+[0])
    answer = INF
    for x,y in trash_list: answer = min(answer,visited[x][y][z_size-1])
    if answer >= INF: answer = -1
    return answer

def get_room(n):
    maze = []
    for _ in range(n):maze.append(list(input()))
    return maze

def get_start(room):
    for x in range(h):
        for y in range(w):
            if room[x][y] == 'o': return [x,y]

def get_trash_list(room,change_list):
    ret_value = []
    idx = 1
    for x in range(h):
        for y in range(w):
            if room[x][y] == '*':
                ret_value.append((x,y))
                change_list[x][y] = idx
                idx *= 2
    return ret_value

def bfs(graph,visited,change,start):
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy,state = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or graph[nx][ny] == 'x':continue
            next_state = state | change[nx][ny]
            if visited[nx][ny][next_state] > visited[vx][vy][state] + 1:
                visited[nx][ny][next_state] = visited[vx][vy][state] + 1
                queue.append((nx,ny,next_state))
                

if __name__ == "__main__":
    INF = int(1e9)
    main()