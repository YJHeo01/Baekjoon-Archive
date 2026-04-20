import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

adj_matrix = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    adj_matrix[a][b] = min(adj_matrix[a][b],c)


path = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        path[i][j] = i
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                path[i][j] = k
                adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj_matrix[i][j] == INF or i == j:
            print(0,end=" ")
        else:
            print(adj_matrix[i][j],end=" ")
    print()

def solution(path,start,end):
    mid = path[start][end]
    if mid == start:
        return [start]
    ret_value = solution(path,start,mid) + [mid]
    return ret_value

for i in range(1,n+1):
    for j in range(1,n+1):
        if adj_matrix[i][j] == INF or i == j:
            print(0)
        else:
            tmp = solution(path,i,j) + [j]
            cnt = len(tmp)
            print(cnt,end=" ")
            for k in tmp:
                print(k,end=" ")
            print()