h,w,x,y = map(int,input().split())
array_B = [list(map(int,input().split())) for _ in range(h)]
array_A = [[0]*w for _ in range(h)]

for i in range(x):
    for j in range(w):
        array_A[i][j] = array_B[i][j]

for i in range(h):
    for j in range(y):
        array_A[i][j] = array_B[i][j]

for i in range(x,h):
    for j in range(y,w):
        array_A[i][j] = array_B[i][j] - array_B[i-x][j-y]

for row in array_A:
    print(*row)