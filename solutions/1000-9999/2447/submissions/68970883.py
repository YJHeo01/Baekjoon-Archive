def recursion(start_x,end_x,start_y,end_y,star):
    if start_x + 1 == end_x:
        return
    dx = (end_x-start_x)//3
    dy = (end_y-start_y)//3
    recursion(start_x,start_x+dx,start_y,start_y+dy,star)
    recursion(start_x,start_x+dx,start_y+dy,start_y+2*dy,star)
    recursion(start_x,start_x+dx,start_y+2*dy,end_y,star)
    recursion(start_x+dx,start_x+2*dx,start_y,start_y+dy,star)
    for i in range(start_x+dx,start_x+2*dx):
        for j in range(start_y+dy,start_y+2*dy):
            star[i][j] = ' '
    recursion(start_x+dx,start_x+2*dx,start_y+2*dy,end_y,star)
    recursion(start_x+2*dx,end_x,start_y,start_y+dy,star)
    recursion(start_x+2*dx,end_x,start_y+dy,start_y+2*dy,star)
    recursion(start_x+2*dx,end_x,start_y+2*dy,end_y,star)
    

    

n = int(input())

answer = [['*']*n for _ in range(n)]

recursion(0,n,0,n,answer)
for i in range(n):
    for j in range(n):
        print(answer[i][j],end='')
    print()