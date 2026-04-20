import sys, math

input = sys.stdin.readline

n,m = map(int,input().split())

k = n * m // 4

answer = [[0]*m for _ in range(n)]

for i in range(k):
    value = i + 1
    x1,y1 = i // int(math.sqrt(k)), i % int(math.sqrt(k))
    if answer[x1][y1] != 0:
        x1,y1 = y1,x1
    x2,y2 = x1, m - 1 - y1
    x3,y3 = n - 1 - x1, m - 1 - y1
    x4,y4 = n-1-x1,y1
    answer[x1][y1] = value
    answer[x2][y2] = value
    answer[x3][y3] = value
    answer[x4][y4] = value
    
for row in answer:
    print(*row)