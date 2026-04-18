h,w = map(int,input().split())

INF = int(1e9)

sky = [list(input()) for _ in range(h)]

time = [[INF]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if sky[i][j] != 'c': continue
        for k in range(j,w):
            time[i][k] = k - j

for i in range(h):
    for j in range(w):
        if time[i][j] == INF:
            print(-1,end=" ")
        else:
            print(time[i][j],end=" ")
    print()