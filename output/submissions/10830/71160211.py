#https://github.com/YJHeo01

n,b = map(int,input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def cal_matrix(matrix_A,matrix_B):
    ret_matrix = []
    for i in range(n):
        tmp_list = []
        for j in range(n):
            tmp = 0
            for x in range(n):
                tmp += matrix_A[i][x] * matrix_B[x][j]
            tmp_list.append(tmp%1000)
        ret_matrix.append(tmp_list)
    return ret_matrix

def solution(matrix,b):
    if b == 1:
        return matrix
    if b % 2 == 0:
        return cal_matrix(solution(matrix,b//2),solution(matrix,b//2))
    else:
        return cal_matrix(cal_matrix(solution(matrix,b//2),solution(matrix,(b//2))),matrix)

answer = solution(matrix,b)

for row in answer:
    for i in row:
        print(i,end=" ")
    print()