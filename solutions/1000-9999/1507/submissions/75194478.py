n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))

road = [[True]*n for _ in range(n)]

impossible = False
for k in range(n):
    for i in range(n):
        if k == i:
            continue
        for j in range(i+1,n):
            if k == j:
                continue
            if matrix[i][j] == matrix[i][k] + matrix[k][j]:
                road[i][j] = False
            elif matrix[i][j] > matrix[i][k] + matrix[k][j]:
                impossible = True
                break
            else:
                continue

answer = 0

for i in range(n):
    for j in range(i+1,n):
        if road[i][j] == True:
            answer += matrix[i][j]
if impossible == True:
    answer = -1

print(answer)