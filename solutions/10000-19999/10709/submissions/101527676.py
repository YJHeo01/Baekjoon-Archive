h,w = map(int,input().split())

sky = [list(input()) for _ in range(h)]

for x in range(h):
    cloud = -1
    for y in range(w):
        if sky[x][y] == 'c': cloud = y
        if cloud == -1: print("-1",end=" ")
        else: print(y-cloud,end=" ")
    print()