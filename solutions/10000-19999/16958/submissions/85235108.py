import sys, heapq

input = sys.stdin.readline

def main():
    special_city = []
    city_position = [(0,0)]
    adj_matrix = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        s,x,y = map(int,input().split())
        if s == 1: special_city.append(i)
        city_position.append((x,y))
    
    for i in range(2,n+1):
        for j in range(1,i):
            a_x, a_y = city_position[i]
            b_x, b_y = city_position[j]
            adj_matrix[i][j] = abs(a_x-b_x) + abs(a_y-b_y)
            adj_matrix[j][i] = adj_matrix[i][j]

    for i in special_city:
        for j in special_city:
            if i == j: continue
            adj_matrix[i][j] = min(adj_matrix[i][j],t)
    
    distance = [[INF]*(n+1)]
    
    for i in range(1,n+1):
        tmp = [INF] * (n+1)
        dijkstra(adj_matrix,tmp,i)
        distance.append(tmp)
    
    m = int(input())

    ans = []
    for _ in range(m):
        a,b = map(int,input().split())
        ans.append(distance[a][b])
    
    sys.stdout.write("\n".join(map(str,ans)))
    
def dijkstra(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]: continue
        for nx in range(1,n+1):
            nd = dist + graph[vx][nx]
            if distance[nx] > nd:
                distance[nx] = nd
                heapq.heappush(q,(nd,nx))

if __name__ == "__main__":
    INF = int(1e9)
    n,t = map(int,input().split())
    main()