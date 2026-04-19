t = int(input())

array = [[0]*15 for _ in range(15)]

for i in range(15):
    array[0][i] = i

for i in range(1,15):
    for j in range(1,15):
        array[i][j] = sum(array[i-1][:j+1])

for _ in range(t):
    k = int(input())
    n = int(input())
    print(array[k][n])