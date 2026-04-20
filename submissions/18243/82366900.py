import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    adj_matrix = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        a,b = map(int,input().split())
        adj_matrix[a][b] = 1
        adj_matrix[b][a] = 1
    for i in range(n+1):
        adj_matrix[i][i] = 0
    for mid in range(1,n+1):
        for left in range(1,n+1):
            for right in range(1,n+1):
                adj_matrix[left][right] = min(adj_matrix[left][right],adj_matrix[left][mid]+adj_matrix[mid][right])
    big = False
    for i in range(1,n+1):
        for j in range(1,n+1):
            if adj_matrix[i][j] >= 7:
                big = True
    if big == True:
        print("Big World!")
    else:
        print("Small World!")


if __name__ == "__main__":
    INF = int(1e9)
    main()