import sys

input = sys.stdin.readline

r,c,q = map(int,input().split())

picture = [list(map(int,input().split())) for _ in range(r)]

prefix_sum = [[0]*(c+1) for _ in range(r+1)]

for i in range(r):
    for j in range(c):
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + picture[i][j]
        
for _ in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    cnt = (r2-r1+1) * (c2-c1+1)
    r1 -= 1; c1 -= 1
    sum_light = prefix_sum[r2][c2]-prefix_sum[r2][c1]-prefix_sum[r1][c2]+prefix_sum[r1][c1]
    print(sum_light//cnt)