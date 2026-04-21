import sys

input = sys.stdin.readline

m,n = map(int,input().split())

answer = [[0]*m for _ in range(m)]
for _ in range(n):
    a,b,c = map(int,input().split())
    i = 0
    for _ in range(b):
        if a < m:
            answer[m-1-a][0] += 1
        else:
            answer[0][a-m+1] += 1
        a += 1
    for _ in range(c):
        if a < m:
            answer[m-1-a][0] += 2
        else:
            answer[0][a-m+1] += 2
        a += 1

for i in range(1,m):
    for j in range(1,m):
        answer[i][j] = max(answer[i-1][j],answer[i][j-1])

for i in range(m):
    for j in range(m):
        print(answer[i][j]+1,end=" ")
    print()