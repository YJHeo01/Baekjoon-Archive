from collections import deque

def main():
    before_picture = get_picture(n)
    after_picture = get_picture(n)
    print(solution(before_picture,after_picture))

def get_picture(n):
    ret_value = []
    for _ in range(n):
        ret_value.append(list(map(int,input().split())))
    return ret_value

def solution(before_picture,after_picture):
    different_cnt = 0
    for i in range(n):
        for j in range(m):
            if before_picture[i][j] != after_picture[i][j]:
                if different_cnt == 1 or bfs(before_picture,after_picture,(i,j)) == False:
                    return "NO"
                different_cnt += 1
    return "YES"

def bfs(before_picture,after_picture,start):
    queue = deque([start])
    x,y = start
    before_color = before_picture[x][y]
    after_color = after_picture[x][y]
    before_picture[x][y] = after_color
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:continue
            if before_picture[nx][ny] == before_color:
                if after_picture[nx][ny] != after_color:
                    return False
                before_picture[nx][ny] = after_color
                queue.append((nx,ny))
    return True

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()