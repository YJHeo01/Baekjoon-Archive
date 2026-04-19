def main():
    n = int(input())
    A = [list(map(int,input().split())) for _ in range(n)]
    for _ in range(int(input())):
        tmp = list(map(int,input().split()))
        if tmp[0] == 1:
            idx = tmp[1] - 1
            A[idx] = [A[idx][n-1]] + A[idx][:n-1]
        else:
            A = get_new_A(A,n)
    for row in A:
        print(*row)

def get_new_A(A,n):
    new_A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_i, new_j = new_position(i,j,n)
            new_A[new_i][new_j] = A[i][j]
    return new_A

def new_position(i,j,n):
    new_i = j
    new_j = n - i - 1
    return new_i, new_j

if __name__ == "__main__":
    main()