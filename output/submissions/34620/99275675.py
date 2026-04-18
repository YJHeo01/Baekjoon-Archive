a,b = map(int,input().split())

if a % b != 1:
    print(-1)
else:
    tmp = 1
    print("G",end="")
    while True:
        if a /b == tmp: break
        if tmp > a / b:
            tmp /= 2
            print("K",end="")
        else:
            tmp+=1
            print("G",end="")