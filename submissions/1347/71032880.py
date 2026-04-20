dx = [1,0,-1,0]
dy = [0,1,0,-1]

direction = 0

def turn_left(d):
    return (d+1)%4

def turn_right(d):
    return (d-1)%4

n = int(input())

command = list(input())

ground = [[0] * 101 for _ in range(101)]
ground[50][50] = '.'
x,y = 50,50

min_x = 50
max_x = 50
min_y = 50
max_y = 50
for i in range(n):
    if command[i] == 'F':
        x += dx[direction]
        y += dy[direction]
        min_x, min_y, max_x, max_y = min(min_x,x), min(min_y,y), max(max_x,x), max(max_y,y)
        ground[x][y] = '.'
    else:
        if command[i] == 'R':
            direction = turn_right(direction)
        else:
            direction = turn_left(direction)

for i in range(min_x,max_x + 1):
    for j in range(min_y,max_y+1):
        if ground[i][j] != 0:
            print('.',end="")
        else:
            print('#',end="")
    print()
