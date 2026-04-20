import sys

input = sys.stdin.readline

n, m = map(int,input().split())

array = []
prefix_sum = [[0]* (n+2) for _ in range(n+2)]

for _ in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j-1] + array[i-1][j-1]
        for k in range(0,i-1):
            prefix_sum[i][j] += array[k][j-1]
        for k in range(0,j-1):
            prefix_sum[i][j] += array[i-1][k]
for i in range(n+1):
    for j in range(n+1):
        print(prefix_sum[i][j],end=" ")
    print()
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(prefix_sum[x2][y2]-prefix_sum[x1-1][y2]-prefix_sum[x2][y1-1]+prefix_sum[x1-1][y1-1])