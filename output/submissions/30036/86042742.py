def main():
    color = list(input())
    stage = [list(input()) for _ in range(N)]
    command = list(input())
    
    dx_dy = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
    ink = 0
    x,y = get_init_xy(stage)
    jump_cnt = 0
    
    for c in command:
        if c == 'j':
            ink += 1
        elif c == 'J':
            Jump(stage,ink,color[jump_cnt],(x,y))
            jump_cnt += 1; jump_cnt %= I; ink = 0
        else:
            dx,dy = dx_dy[c]
            nx,ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N or stage[nx][ny] != '.': continue
            stage[x][y], stage[nx][ny] = '.', '@'
            x,y = nx, ny

    for i in range(N):
        for j in range(N):
            print(stage[i][j],end="")
        print()

def get_init_xy(stage):
    for i in range(N):
        for j in range(N):
            if stage[i][j] == '@': return (i,j)

def Jump(stage,ink,color,position):
    x,y = position
    for dx in range(-ink,ink+1):
        nx = x + dx
        if nx < 0: continue
        if nx >= N: break
        left = max(0,y-ink+abs(dx))
        right = min(N-1,y+ink-abs(dx))
        for ny in range(left,right+1):
            if stage[nx][ny] != '.' and stage[nx][ny] != '@': stage[nx][ny] = color

if __name__ == "__main__":
    I, N, K = map(int,input().split())
    main()