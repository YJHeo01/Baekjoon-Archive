import sys

input = sys.stdin.readline

n,m = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(n)]

x, y = -1,-1

for i in range(n):
    for j in range(n):
        if maze[i][j] == 2:
            x = i
            y = j

event = dict()

for c in ['W','A','S','D']:
    tmp = input().rstrip()
    event[c] = tmp

frame = ['0'] + list(input().rstrip())

move = dict()

move['W'] = (-1,0)
move['A'] = (0,-1)
move['S'] = (1,0)
move['D'] = (0,1)

for i in range(1,m+1):
    for key in ['W','A','S','D']:
        dx,dy = 0,0
        if event[key] == "Down":
            if frame[i-1] != key and frame[i] == key:
                dx,dy = move[key]
        elif event[key] == "Stay":
            if frame[i-1] == key and frame[i] == key:
                dx,dy = move[key]
        else:
            if frame[i-1] == key and frame[i] != key:
                dx,dy = move[key]
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= n or maze[nx][ny]==1: continue
        x = nx
        y = ny

print(x+1,y+1)

