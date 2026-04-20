n,q = map(int,input().split())

ground = [0]*(n+1)

for i in range(q):
    x = int(input())
    x_ = x
    while(1):
        if ground[x_] == 1:
            print(x_)
            break
        if x_ == 1:
            ground[x] = 1
            print(x_-1)
            break
        x_ = x_ // 2