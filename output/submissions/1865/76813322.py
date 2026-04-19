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
    edges = []
    for _ in range(m):
        edges.append(list(map(int,input().split())))
    for _ in range(w):
        tmp = list(map(int,input().split()))
        tmp[2] *= -1
        edges.append(tmp)    
    solution(edges,distance)
    answer = 'NO'
    for i in range(1,n+1):
        if distance[i][i] < 0:
            answer = 'YES'
            break
    print(answer)