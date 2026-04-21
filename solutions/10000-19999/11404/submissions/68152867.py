import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
array = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    
    array[a][b] = min(c,array[a][b])

for a in range(1,n+1):
    array[a][a] = 0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            array[a][b] = min(array[a][b],array[a][k] + array[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if array[i][j] == INF:
            print("0",end=' ')
        else : print(array[i][j],end = ' ')
    print()