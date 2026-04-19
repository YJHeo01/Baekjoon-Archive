def main():
    n = int(input())
    print(solution(n))
    
def solution(n):
    x,y = map(int,input().split())
    matrix = get_matrix(x)
    for _ in range(n-1):
        new_x, new_y = map(int,input().split())
        if y != new_x: return -1
        new_matrix = get_matrix(new_x)
        matrix = matrix_multiplication(matrix,new_matrix,x,y,new_y)
        y = new_y
    ret_value = 0
    for i in range(x):
        for j in range(y):
            ret_value += matrix[i][j]
            ret_value %= INF
    return ret_value

def get_matrix(x):
    matrix = []
    for _ in range(x):
        matrix.append(list(map(int,input().split())))
    return matrix

def matrix_multiplication(A,B,x,mid,y):
    new_matrix = [[0]*y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(mid):
                new_matrix[i][j] += A[i][k] * B[k][j]
            new_matrix[i][j] %= INF
    return new_matrix

if __name__ == "__main__":
    INF = 1000000007
    main()