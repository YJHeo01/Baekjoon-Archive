import sys

input = sys.stdin.readline 

INF = int(1e9)

tc = int(input())

def solution(edges,distance):
    for _ in range(n):
        for mid, end, cost in edges:
            for start in range(1,n+1):
                if distance[start][mid] >= INF:
                    continue
                if distance[start][end] > distance[start][mid] + cost:
                    distance[start][end] = distance[start][mid] + cost

for _ in range(tc):
    n,m,w = map(int,input().split())
    distance = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        distance[i][i] = 0
    for _ in range(m):
        a,b,c = map(int,input().split())
        distance[a][b] = min(distance[a][b],c)
        distance[b][a] = min(distance[b][a],c)
    for _ in range(w):
        a,b,c = map(int,input().split())
        c *= -1
        distance[a][b] = min(distance[a][b],c)
    edges = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] >= INF or i == j:
                continue
            edges.append([i,j,distance[i][j]])
    solution(edges,distance)
    answer = 'NO'
    for i in range(1,n+1):
        if distance[i][i] < 0:
            answer = 'YES'
            break
    print(answer)