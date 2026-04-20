import sys

input = sys.stdin.readline

m,n = map(int,input().split())

answer = [[1]*m for _ in range(m)]

for _ in range(n):
    a,b,c = map(int,input().split())
    one_x, one_y, two_x, two_y = m,m,m,m
    for i in range(1,2*m):
        if i <= a:
            continue
        elif i <= (a+b):
            if i > m:
                one_x = min(one_x,i-m)
                answer[0][i-m] += 1
            elif i < m:
                one_y = min(one_y,m-i)
                answer[m-i][0] += 1
            else:
                one_x = 0
                one_y = 0
                answer[0][0] += 1
        else:
            if i > m:
                two_x = min(two_x,i-m)
                answer[0][i-m] += 2
            elif i < m:
                two_y = min(two_y,m-i)
                answer[m-i][0] += 2
            else:
                two_x = 0
                two_y = 0
                answer[0][0] += 2
    for i in range(1,m):
        for j in range(1,m):
            if i >= two_y or j >= two_x:
                answer[i][j] += 2
            elif i >= one_y or j >= one_x:
                answer[i][j] += 1
            else:
                continue
for i in range(m):
    for j in range(m):
        print(answer[i][j],end=" ")
    print()