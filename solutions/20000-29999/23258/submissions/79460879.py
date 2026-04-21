import sys

input = sys.stdin.readline

def main():
    n,q = map(int,input().split())
    adj_matrix = [[]]
    for _ in range(n):
        adj_matrix.append([0] + list(map(int,input().split())))
    time = [[[0]*(n+1) for _ in range(n+1)]for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if adj_matrix[i][j] == 0: time[0][i][j] = INF
            else: time[0][i][j] = adj_matrix[i][j]
    
    for c in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                time[c][i][j] = time[c-1][i][j]
        for k in range(1,c):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    time[c][i][j] = min(time[c][i][j],time[c][i][k]+time[c][k][j])
    
    for _ in range(q):
        c,s,e = map(int,input().split())
        answer = time[c][s][e]
        if answer >= INF: answer = -1
        print(answer)

if __name__ == "__main__":
    INF = int(1e9)
    main() 