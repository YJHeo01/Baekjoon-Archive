import sys

input = sys.stdin.readline

def main():
    edges = []
    cost = [-INF] * (n+1)
    reverse_road = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        reverse_road[v].append((u,w))
        edges.append([u,v,w])
    for i in solution(edges,cost,reverse_road):
        print(i,end=" ")


def solution(edges,cost,reverse_road):
    cost[1] = 0
    for _ in range(n-1):
        for u,v,w in edges:
            if cost[u] + w > cost[v]:
                cost[v] = cost[u] + w
    for u,v,w in edges:
        if cost[u] + w > cost[v]:
            return [-1]
    if cost[n] == -INF:
        return [-1]
    
    retValue = [n]
    vx = n
    while True:
        for nx,w in reverse_road[vx]:
            if w == 0: continue
            if cost[nx] + w == cost[vx]:
                vx = nx
                break
        retValue.append(vx)
        if vx == 1: break
    
    retValue.reverse()
    return retValue
    
                
if __name__ == "__main__":
    INF = int(1e9)
    n,m = map(int,input().split())
    main()