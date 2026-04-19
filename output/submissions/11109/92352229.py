for _ in range(int(input())):
    d,n,s,p=map(int,input().split())
    a=p*n+d;b=s*n
    if a>b:print("do not parallelize")
    elif a<b:print("parallelize")
    else:print("does not matter")