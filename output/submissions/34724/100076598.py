n,m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

mat = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat[i][j] = int(arr[i][j])

answer = 0

for i in range(1,n):
    for j in range(1,m):
        tmp = 1
        for dx in range(-1,1):
            for dy in range(-1,1):
                tmp = min(tmp,mat[i+dx][j+dy])
        answer = max(answer,tmp)

print(answer)