t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    xx = ((n-1)//h)+1
    yy = ((n-1)%h)+1
    print(yy,end='')
    if xx < 10:
        print("0",end='')
    print(xx)