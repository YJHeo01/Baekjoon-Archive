#https://github.com/YJHeo01]

n,m = map(int,input().split())

matrix_A = []
for _ in range(n):
    matrix_A.append(list(map(int,input().split())))

m,k = map(int,input().split())

matrix_B = []

for _ in range(m):
    matrix_B.append(list(map(int,input().split())))

matrix_answer = []

for i in range(n):
    tmp_list = []
    for j in range(k):
        tmp = 0
        for x in range(m):
            tmp += matrix_A[i][x] * matrix_B[x][j]
        tmp_list.append(tmp)
    matrix_answer.append(tmp_list)

for row in matrix_answer:
    for answer in row:
        print(answer,end=" ")
    print()