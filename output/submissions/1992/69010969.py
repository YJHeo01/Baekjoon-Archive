def recursion(start_x,end_x,start_y,end_y,image):
    if start_x + 1 == end_x:
        print(image[start_x][start_y],end="")
        return
    n = image[start_x][start_y]
    for i in range(start_x,end_x):
        for j in range(start_y,end_y):
            if n!= image[i][j]:
                print('(',end="")
                mid_x = (start_x+end_x)//2
                mid_y = (start_y+end_y)//2
                recursion(start_x,mid_x,start_y,mid_y,image)
                recursion(start_x,mid_x,mid_y,end_y,image)
                recursion(mid_x,end_x,start_y,mid_y,image)
                recursion(mid_x,end_x,mid_y,end_y,image)
                print(')',end="")
                return
    print(n,end="")



n = int(input())
mp4 = []
for i in range(n):
    tmp = list(input())
    mp4.append(tmp)

recursion(0,n,0,n,mp4)