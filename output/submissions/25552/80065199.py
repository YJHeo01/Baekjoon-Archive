from collections import deque
import sys

input = sys.stdin.readline

def main():
    init_grass = get_grass()
    d = int(input())
    result_grass = get_grass()
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if init_grass[i][j] == 'O' and visited[i][j] == False:
                visited[i][j] = True
                solution(result_grass,visited,(i,j),d)
    answer = 'YES'
    for i in range(n):
        for j in range(m):
            if (result_grass[i][j] == 'O' and visited[i][j] == False) or (result_grass[i][j] == 'X' and visited[i][j] == True):
                answer = 'NO'
                break
    print(answer)

def get_grass():
    grass = []
    for _ in range(n):
        grass.append(list(input()))
    return grass

def solution(result_grass,visited,start,d):
    queue = deque([start])
    while queue:
        vx,vy = queue.popleft()
        for length in range(d+1):
            for dx in range(length+1):
                nx = vx + dx
                if nx >= n: break
                dy = length - dx
                queue += move_grass(result_grass,visited,(nx,vy),dy)
            for dx in range(-1,-length-1,-1):
                nx = vx + dx
                if nx < 0: break
                dy = length + dx
                queue += move_grass(result_grass,visited,(nx,vy),dy)


def move_grass(result_grass,visited,point,dy):
    ret_value = []
    x,vy = point
    y = vy
    for _ in range(dy+1):
        if y >= m: break
        if visited[x][y] == False and result_grass[x][y] == 'O':
            visited[x][y] = True
            ret_value.append((x,y))
        y += 1
    y = vy
    for _ in range(dy+1):
        if y < 0: break
        if visited[x][y] == False and result_grass[x][y] == 'O':
            visited[x][y] = True
            ret_value.append((x,y))
        y -= 1
    return ret_value

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()