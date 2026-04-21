n,q = map(int,input().split())

ground = [0]*(n+1)
block = 0
for i in range(q):
    x = int(input())
    x_ = x
    while(x_ >= 2):
        if ground[x_] == 1:
            block = x_
        x_ = x_ // 2
    print(block)
    if block != 0:
        ground[block] = 1
        block = 0
    else:
        ground[x] = 1