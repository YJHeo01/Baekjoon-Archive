blue, white = 0, 0

def check_paper(x1,x2,y1,y2):
    global blue,white
    white_ = 0
    blue_ = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if paper[i][j] == 1:
                blue_ += 1
            else:
                white_ += 1
    if blue_ == 0:
        white += 1
    elif white_ == 0:
        blue += 1
    else:
        mid_x = (x1+x2)//2
        mid_y = (y1+y2)//2
        check_paper(x1,mid_x,y1,mid_y)
        check_paper(mid_x+1,x2,y1,mid_y)
        check_paper(x1,mid_x,mid_y+1,y2)
        check_paper(mid_x+1,x2,mid_y+1,y2)
n = int(input())

paper = []

for i in range(n):
    tmp = list(map(int,input().split()))
    paper.append(tmp)

check_paper(0,7,0,7)
print(white)
print(blue)