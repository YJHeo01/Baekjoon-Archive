import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = int(1e9)

def main():
    global n
    n,m = map(int,input().split())
    graph = get_graphs(n,m)
    distance = [-INF] * (n+1)
    not_exist_path = bellman_ford(graph,distance,n)
    if not_exist_path == True:
        print(-1)
    else:
        answer = get_answer(graph,distance,1)
        while answer:
            i = answer.pop()
            print(i,end=" ")

def get_graphs(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
    return graph

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

def get_answer(graph,distance,vx):
    if vx == n: return [n]
    ret_value = []
    for nx, cost in graph[vx]:
        if distance[nx] == distance[vx] + cost:
            ret_value = get_answer(graph,distance,nx)
            if ret_value != []: return ret_value + [vx]
    return ret_value 

if __name__ == "__main__":
    main()