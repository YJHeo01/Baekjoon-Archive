#밤편지 23258번

import sys

input = sys.stdin.readline

def main():
    n,q = map(int,input().split())
    adj_matrix = [list(map(int,input().split())) for _ in range(n)]
    distance = [[[INF]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 0: continue
            distance[i+1][j+1][0] = adj_matrix[i][j]
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                distance[i][j][k] = min(distance[i][j][k-1],distance[i][k][k-1]+distance[k][j][k-1])

    for _ in range(q):
        c,s,e = map(int,input().split())
        answer = distance[s][e][c-1]
        if answer >= INF: answer = -1
        print(answer)

if __name__ == "__main__":
    INF = sys.maxsize
    main()