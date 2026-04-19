import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    adj_matrix = get_adj_matrix(n)
    adj_matrix = floyd(adj_matrix,n)
    for _ in range(m):
        a,b,c = map(int,input().split())
        if adj_matrix[a-1][b-1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")
        
def get_adj_matrix(n):
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int,input().split())))
    return adj_matrix

def floyd(matrix,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
    return matrix

if __name__ == "__main__":
    main()