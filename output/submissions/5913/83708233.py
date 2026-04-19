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
    
    if apple_cnt == 25: return check_meet(Junkyu,Haebin)
    
    ret_value = 0
    
    if apple_cnt % 2 == 0:
        vx,vy = Junkyu
    else:
        vx,vy = Haebin

    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        nx = vx + dx
        ny = vy + dy
        if nx <= 0 or ny <= 0 or nx > 5 or ny > 5 or visited[nx][ny] == True: continue
        visited[nx][ny] = True
        if apple_cnt % 2 == 0:
            ret_value += solution(visited,(nx,ny),Haebin,apple_cnt + 1)
        else:
            ret_value += solution(visited,Junkyu,(nx,ny),apple_cnt+1)
        visited[nx][ny] = False
    
    return ret_value

def check_meet(Junkyu,Haebin):
    vx,vy = Haebin
    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        if Junkyu == (vx+dx,vy+dy):
            return 1
    return 0

if __name__ == "__main__":
    main()