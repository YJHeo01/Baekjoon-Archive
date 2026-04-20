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
            print("0")
            break
        if x_ % 2 == 0:
            x_ = x_ // 2
        else: x_ -= 1