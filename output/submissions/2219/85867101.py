import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    adj_matrix = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        adj_matrix[a][b], adj_matrix[b][a] = c,c
    for i in range(n+1): adj_matrix[i][i] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])
    time = []
    for i in range(n+1): time.append(sum(adj_matrix[i]))
    answer = 0
    for i in range(1,n+1):
        if time[answer] > time[i]:
            answer = i
    print(answer)

if __name__ == "__main__":
    INF = int(1e9)
    main()