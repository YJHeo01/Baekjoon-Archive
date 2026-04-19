import sys

input = sys.stdin.readline

INF = 100000

def main():
    n,m = map(int,input().split())
    edges, reverse_graph = get_graphs(n,m)
    distance = [-INF] * (n+1)
    not_exist_path = bellman_ford(edges,distance,n)
    if not_exist_path == True:
        print(-1)
    else:
        answer = get_answer(reverse_graph,distance,n)
        for i in answer:
            print(i,end=" ")

def get_graphs(n,m):
    edges = []
    reverse_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        edges.append((u,v,w))
        reverse_graph[v].append((u,w))
    return edges, reverse_graph

def bellman_ford(edges,distance,n):
    distance[1] = 0
    for i in range(n):
        for start, end, cost in edges:
            if distance[end] < distance[start] + cost:
                distance[end] = distance[start] + cost
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