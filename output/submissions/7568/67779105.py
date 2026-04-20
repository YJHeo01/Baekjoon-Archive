N = int(input())
ranking = [1]*N
xy = []
for i in range(N):
    x, y = map(int,input().split())
    xy.append((x,y))

for i in range(N):
    for j in range(N):
        if xy[i][0] < xy[j][0]:
            if xy[i][1] < xy[j][1]:
                ranking[i] += 1

for i in range(N):
    print(ranking[i], end=' ')