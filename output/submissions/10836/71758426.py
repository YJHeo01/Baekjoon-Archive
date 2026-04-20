import sys

input = sys.stdin.readline

m,n = map(int,input().split())

answer = [[1]*m for _ in range(m)]
grow_value = [[0]*m for _ in range(m)]
for _ in range(n):
    a,b,c = map(int,input().split())
    for i in range(a,a+b):
        if i < m:
            grow_value[m-1-i][0] += 1
            answer[m-1-i][0] += 1
        else:
            grow_value[0][i-m+1] += 1
            answer[0][i-m+1] += 1
    for i in range(a+b,2*m-1):
        if i < m:
            grow_value[m-1-i][0] += 2
            answer[m-1-i][0] += 2
        else:
            grow_value[0][i-m+1] += 2
            answer[0][i-m+1] += 2

for i in range(1,m):
    for j in range(1,m):
        grow_value[i][j] = max(grow_value[i-1][j],grow_value[i][j-1],grow_value[i-1][j-1])
        answer[i][j] += grow_value[i][j]

for i in range(m):
    for j in range(m):
        print(answer[i][j],end=" ")
    print()