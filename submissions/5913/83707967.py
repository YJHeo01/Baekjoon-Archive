def main():
    visited = [[False]*6 for _ in range(6)]
    k = int(input())
    for _ in range(k):
        a,b = map(int,input().split())
        visited[a][b] = True
    visited[1][1] = True; visited[5][5] = True
    answer = solution(visited,(1,1),(5,5),k+2)
    print(answer)
def solution(visited,Junkyu,Haebin,apple_cnt):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    if apple_cnt == 25:
        vx,vy = Haebin
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if (nx,ny) == Junkyu: return 1
        return 0
    ret_value = 0
    
    if apple_cnt % 2 == 0:
        vx,vy = Junkyu
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > 5 or ny > 5 or visited[nx][ny] == True: continue
            visited[nx][ny] = True
            ret_value += solution(visited,(nx,ny),Haebin,apple_cnt + 1)
            visited[nx][ny] = False
    else:
        vx,vy = Haebin
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx <= 0 or ny <= 0 or nx > 5 or ny > 5 or visited[nx][ny] == True:continue
            visited[nx][ny] = True
            ret_value += solution(visited,Junkyu,(nx,ny),apple_cnt+1)
            visited[nx][ny] = False
    return ret_value

if __name__ == "__main__":
    main()