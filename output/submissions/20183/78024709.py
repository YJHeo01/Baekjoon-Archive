import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    graph = get_graph()
    max_max_cost = [[0,INF] for _ in range(n+1)]
    answer = get_answer(graph,max_max_cost)
    if answer >= INF:
        answer = -1
    print(answer)

def get_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    return graph

def get_answer(graph,max_max_cost):
    q = []; heapq.heappush(q,(0,0,a))
    max_max_cost[a][1] = 0
    ret_value = INF
    while q:
        max_cost, sum_cost, vx = heapq.heappop(q)
        if max_cost > max_max_cost[vx][0]:
            continue
        for nx, cost in graph[vx]:
            next_max_cost, next_sum_cost = max(max_cost,cost), sum_cost + cost
            if next_sum_cost > c or next_max_cost > ret_value: continue
            if nx == b: ret_value = next_max_cost; continue
            if next_max_cost > max_max_cost[nx][0]:
                if next_sum_cost >= max_max_cost[nx][1]: continue
                max_max_cost[nx][0] = next_max_cost; max_max_cost[nx][1] = next_sum_cost
            else:
                if max_max_cost[nx][1] >= next_sum_cost:
                    max_max_cost[nx][1] = next_sum_cost; max_max_cost[nx][0] = next_max_cost
            
            heapq.heappush(q,(next_max_cost,next_sum_cost,nx))
    return ret_value

if __name__ == "__main__":
    n,m,a,b,c = map(int,input().split())
    main()