from collections import deque

def control_d(d):
    d  = d % 4
    return d

def snake(t,board,direction,n):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    d_index = 1
    last_i = 0
    x,y = 0,0
    board[y][x] = 2
    s=0
    queue_x = deque([x])
    queue_y = deque([y])
    m = 0
    for i in t:
        for j in range(last_i,i):
            x += dx[d_index]
            y += dy[d_index]
            m+=1
            if x < 0 or y < 0 or x >= n or y>= n:
                return m
            queue_x.append(x)
            queue_y.append(y)
            if board[y][x] == 1:
                board[y][x] = 0
            elif board[y][x] == 2:
                return m
            else:
                v_x = queue_x.popleft()
                v_y = queue_y.popleft()
                board[v_y][v_x] = 0
            board[y][x] = 2        
        if direction[s] == 'D':
            d_index = control_d(d_index + 1)
        else: d_index = control_d(d_index-1)
        s+=1
        last_i = i


n = int(input())
k = int(input())
s = 0
direction = []
t = []
board = [ [0] * n for _ in range(n) ]
for i in range(k):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
l = int(input())
for i in range(l):
    a, b= input().split()
    t.append(int(a))
    direction.append(b)
t.append(100)
direction.append(b)

answer = snake(t,board,direction,n)

print(answer)