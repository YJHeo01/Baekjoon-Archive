h,w,x,y = map(int,input().split())
array_B = [list(map(int,input().split())) for _ in range(h+x)]
array_A = [[0]*w for _ in range(h)]

for i in range(x):
    for j in range(w):
        array_A[i][j] = array_B[i][j]

for i in range(h):
    for j in range(y):
        array_A[i][j] = array_B[i][j]

for i in range(h,h+x):
    for j in range(w):
        array_A[i-x][j] = array_B[i][j+y]

for i in range(h):
    for j in range(w,w+y):
        array_A[i][j-y] = array_B[i+x][j]

for row in array_A:
    print(*row)