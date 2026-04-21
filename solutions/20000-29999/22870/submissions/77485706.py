import sys, heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    global n,m,s,e
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    s,e = map(int,input().split())
    distance = [INF] * (n+1)
    dijkstra_s_to_e(graph,distance,s)
    answer = distance[e]
    shortest_path_list = search_shortest_path(graph,distance,[e])
    shortest_path_list.sort()
    shortest_path = shortest_path_list[0]
    prohabit_edge = get_prohabit_edge(shortest_path)
    distance = [INF] * (n+1)
    dijkstra_e_to_s(graph,distance,prohabit_edge,e)
    answer += distance[s]
    print(answer)    

def dijkstra_s_to_e(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

def search_shortest_path(graph,distance,path):
    vx = path[0]
    if vx == s:
        return path
    ret_value = []
    for nx, length in graph[vx]:
        if distance[nx] + length == distance[vx]:
            if vx == e:
                ret_value.append(search_shortest_path(graph,distance,[nx]+path))
            else:
                ret_value += search_shortest_path(graph,distance,[nx]+path)
    return ret_value

def get_prohabit_edge(shortest_path):
    shortest_path_node_cnt = len(shortest_path)
    prohabit_edge = [[] for _ in range(n+1)]
    prohabit_edge[shortest_path[0]].append(shortest_path[1])
    prohabit_edge[shortest_path[shortest_path_node_cnt-1]].append(shortest_path[shortest_path_node_cnt-2])
    for i in range(1,shortest_path_node_cnt-1):
        prohabit_edge[shortest_path[i]].append(shortest_path[i+1])
        prohabit_edge[shortest_path[i]].append(shortest_path[i-1])
    return prohabit_edge

def dijkstra_e_to_s(graph,distance,prohabit_edge,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if nx in prohabit_edge[vx]:
                continue
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

if __name__ == "__main__":
    main()