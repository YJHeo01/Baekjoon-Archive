n,m = map(int,input().split())
array = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y,d = map(int,input().split())
    start_x, start_y, end_x, end_y = 0,0,0,0
    if d == 1:
        start_x, start_y, end_x, end_y = 0,y,x-1,y
    elif d == 2:
        start_x, start_y, end_x, end_y = 0,y+1,x-1,n
    elif d == 3:
        start_x, start_y, end_x, end_y = x,y+1,x,n
    elif d == 4:
        start_x, start_y, end_x, end_y = x+1,y+1,n,n
    elif d == 5:
        start_x, start_y, end_x, end_y = x+1,y,n,y
    elif d == 6:
        start_x, start_y, end_x, end_y = x+1,0,n,y-1
    elif d == 7:
        start_x, start_y, end_x, end_y = x,0,x,y-1
    else:
        start_x, start_y, end_x, end_y = 0,0,x-1,y-1
    for i in range(start_x,end_x+1):
        for j in range(start_y,end_y+1):
            array[i][j] += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if array[i][j] == m:
            print(i,j)
            exit(0)