import heapq

def main():
    array = list(map(int,input().split()))
    distance = [[-1]*3 for _ in range(n)]
    dijkstra(array,distance)
    answer = max(distance[n-1])
    print(answer)

def dijkstra(graph,distance):
    q = []
    heapq.heappush(q,(0,0,0))
    distance[0][0] = 0
    dx = [1,-1]
    while q:
        dist, change_cnt, vx = heapq.heappop(q)
        dist *= -1
        if graph[vx] == 0 or distance[vx][change_cnt] > dist or vx == n-1: continue
        if change_cnt != 2 and dist > distance[vx][change_cnt+1]:
            distance[vx][change_cnt+1] = dist
            heapq.heappush(q,(-dist,change_cnt+1,vx))
        i = change_cnt % 2
        nx = vx + graph[vx] * dx[i]
        if nx < 0 or nx >= n or distance[nx][change_cnt] >= dist + 1: continue
        distance[nx][change_cnt] = dist + 1
        heapq.heappush(q,(-dist-1,change_cnt,nx))

if __name__ == "__main__":
    n = int(input())
    main()
