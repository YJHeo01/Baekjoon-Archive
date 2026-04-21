import sys

input = sys.stdin.readline 

INF = int(1e9)

n,m = map(int,input().split())

distance = [INF] * (n+1)
edges = []

for _ in range(m):
    edges.append(list(map(int,input().split())))

def bellman_ford(edges,distance,start):
    distance[start] = 0
    for _ in range(n-1):
        for a,b,cost in edges:
            if distance[a] >= INF:
                continue
            if distance[b] > distance[a] + cost:
                distance[b] = distance[a] + cost

bellman_ford(edges,distance,1)

def check_negative_distance(edges,distance):
    for a,b,cost in edges:
        if distance[b] > distance[a] + cost:
            return True
    return False

if check_negative_distance(edges,distance) == True:
    print(-1)
else:
    for answer in distance[2:]:
        if answer >= INF:
            print(-1)
        else:
            print(answer)