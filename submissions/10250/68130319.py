t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    xx = n % h
    yy = (n // h) + 1
    print(xx,end='')
    if yy < 10:
        print("0",end='')
    print(yy)