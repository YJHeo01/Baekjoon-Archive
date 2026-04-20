import sys

input = sys.stdin.readline

tc = int(input())
INF = int(1e9)
global w,m
def bellman_ford(edges,distance,start):
    distance[start] = 0
    for i in range(n):
        for j in range(w+m):
            start, end, edge_length = edges[j]
            if distance[end] > distance[start] + edge_length:
                distance[end] = distance[start] + edge_length
                if i == n-1:
                    return True
        if distance[start] < 0:
            return True
    return False


for _ in range(tc):
    n,m,w = map(int,input().split())
    edges = []
    for _ in range(m):
        s,e,t = map(int,input().split())    
        edges.append((s,e,t))
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))
    distance = [INF] * (n+1)
    answer_yes = False
    for i in range(1,n+1):
        answer_yes = bellman_ford(edges,distance,i)
        if answer_yes == True:
            break
    if answer_yes == True:
        print("YES")
    else:
        print("NO")
