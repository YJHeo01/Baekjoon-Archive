import sys

input = sys.stdin.readline

m,n = map(int,input().split())

answer = [[0]*m for _ in range(m)]
for _ in range(n):
    a,b,c = map(int,input().split())
    for i in range(a,a+b):
        if i < m:
            answer[m-1-i][0] += 1
        else:
            answer[0][i-m+1] += 1
    for i in range(a+b,2*m-1):
        if i < m:
            answer[m-1-i][0] += 2
        else:
            answer[0][i-m+1] += 2

for i in range(1,m):
    for j in range(1,m):
        answer[i][j] = max(answer[i-1][j],answer[i][j-1])

for i in range(m):
    for j in range(m):
        print(answer[i][j]+1,end=" ")
    print()