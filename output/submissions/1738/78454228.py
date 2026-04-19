import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    n,m = map(int,input().split())
    graph, reverse_graph = get_graphs(n,m)
    distance = [-INF] * (n+1)
    not_exist_path = bellman_ford(graph,distance,n)
    if not_exist_path == True:
        print(-1)
    else:
        answer = get_answer(reverse_graph,distance,n)
        for i in answer:
            print(i,end=" ")

def get_graphs(n,m):
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        reverse_graph[v].append((u,w))
    return graph, reverse_graph

def bellman_ford(graph,distance,n):
    distance[1] = 0
    for i in range(n):
        for mid in range(1,n+1):
            if distance[mid] == -INF: continue
            for end, money in graph[mid]:
                if distance[mid] + money > distance[end]: 
                    distance[end] = distance[mid] + money
                    if i == n-1: return True
    return False

def get_answer(reverse_graph,distance,n):
    ret_value = [n]
    vx = n
    while True:
        for nx, cost in reverse_graph[vx]:
            if distance[nx] + cost == distance[vx]:
                ret_value.append(nx)
                vx = nx 
                break
        if vx == 1: break
    ret_value.reverse()
    return ret_value

if __name__ == "__main__":
    main()