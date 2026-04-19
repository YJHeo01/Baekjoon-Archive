import sys

input = sys.stdin.readline 

INF = int(1e9)

tc = int(input())

def solution(edges,distance,start):
    distance[start] = 0
    for _ in range(n):
        for mid, end, cost in edges:
            if distance[mid] >= INF:
                continue
            if distance[end] > distance[mid] + cost:
                distance[end] = distance[mid] + cost
    if distance[start] < 0:
        return 'YES'
    else:            
        return 'NO'

for _ in range(tc):
    n,m,w = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        edges.append([a,b,c])
        edges.append([b,a,c])
    for _ in range(w):
        a,b,c = map(int,input().split())
        c *= -1
        edges.append([a,b,c])
    answer = 'NO'
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        answer = solution(edges,distance,i)
        if answer == 'YES':
            break
    print(answer)