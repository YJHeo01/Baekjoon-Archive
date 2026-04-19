import heapq

INF = int(1e9)

n,p,k = map(int,input().split())

max_cable_cost = [[INF]*(k+1) for _ in range(n+1)]

for i in range(k+1):
    max_cable_cost[1][i] = 0

cable = [[] for _ in range(n+1)]

for _ in range(p):
    a,b,c = map(int,input().split())
    cable[a].append((b,c))
    cable[b].append((a,c))

def solution(graph,max_cable_cost_list):
    prior_q = []
    heapq.heappush(prior_q,(0,k,1))
    while prior_q:
        max_cost, free_cnt, vx = heapq.heappop(prior_q)
        if max_cost > max_cable_cost_list[vx][free_cnt]:
            continue
        for nx, new_network_cost in graph[vx]:
            new_max_value = max(max_cost,new_network_cost)
            if max_cable_cost_list[nx][free_cnt] > new_max_value:
                max_cable_cost_list[nx][free_cnt] = new_max_value
                heapq.heappush(prior_q,(new_max_value,free_cnt,nx))
            if free_cnt == 0:
                continue
            if max_cable_cost_list[nx][free_cnt-1] > max_cost:
                max_cable_cost_list[nx][free_cnt-1] = max_cost
                heapq.heappush(prior_q,(max_cost,free_cnt-1,nx))

solution(cable,max_cable_cost)

answer = min(max_cable_cost[n])

if answer >= INF:
    answer = -1
    
print(answer)