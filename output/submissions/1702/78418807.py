import sys, heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    graph = get_graph()
    distance = [[INF]*10001 for _ in range(n+1)]
    dijkstra(graph,distance,s)
    answer = get_answer(distance,e)
    print(answer)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        p,r,c,t = map(int,input().split())
        graph[p].append((r,c,t))
        graph[r].append((p,c,t))
    return graph

def dijkstra(graph,distance,start):
    max_time, max_cost = [0] * (n+1), [0] * (n+1)
    min_cost = [INF] * (n+1); min_cost[start] = 0
    q = []
    heapq.heappush(q,(0,0,start))
    while q:
        vt, vc, vx = heapq.heappop(q)
        if vt > max_time[vx] or vc > max_cost[vx] or vt > distance[vx][vc]: continue
        for nx, dc, dt in graph[vx]:
            nt = vt + dt; nc = vc + dc
            if nt >= distance[nx][nc]: continue
            distance[nx][nc] = nt
            heapq.heappush(q,(nt,nc,nx))
            if nt > max_time[nx]:
                if nc >= min_cost[nx]: continue
                max_time[nx] = nt; min_cost[nx] = nc
            if nc > max_cost[nx]:
                if nt > distance[nx][max_cost[nx]]: continue
                max_cost[nx] = nc

def get_answer(distance,end):
    answer = 0
    last_cost = 0
    for i in range(10001):
        if distance[end][i] >= INF: continue
        if distance[end][last_cost] > distance[end][i]:
            answer += 1
            last_cost = i
    return answer

if __name__ == "__main__":
    n,m,s,e = map(int,input().split())
    main()