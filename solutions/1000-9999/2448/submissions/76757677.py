n = int(input())

c = n*2 - 1
star = [[' '] * c for _ in range(n)]

mid = c // 2

def draw_star(star,x,y):
    for dx in range(3):
        for dy in range(-dx,dx+1):
            nx = x + dx
            ny = y + dy
            star[nx][ny] = '*'
    star[x+1][y] = ' '

def top_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y - 3
    third_floor_left_star(star,nx,ny)
    ny = y + 3
    third_floor_right_star(star,nx,ny)

def third_floor_left_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y - 3
    second_floor_left_star(star,nx,ny)

def second_floor_left_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y - 3
    first_floor_left_star(star,nx,ny)
    ny = y + 3
    first_floor_mid_star(star,nx,ny)

def first_floor_left_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y - 3
    top_star(star,nx,ny)
    
def first_floor_mid_star(star,x,y):
    draw_star(star,x,y)

def third_floor_right_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y + 3
    second_floor_right_start(star,nx,ny)

def second_floor_right_start(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y - 3
    first_floor_mid_star(star,nx,ny)
    ny = y + 3
    first_floor_right_star(star,nx,ny)

def first_floor_right_star(star,x,y):
    draw_star(star,x,y)
    nx = x + 3
    if nx == n:
        return
    ny = y + 3
    top_star(star,nx,ny)
    
top_star(star,0,mid)

for i in range(n):
    for j in range(c):
        print(star[i][j],end="")
    print()