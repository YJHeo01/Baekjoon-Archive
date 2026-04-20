import heapq, sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    global n
    n = int(input())
    start = list(map(int,input().split()))
    distance = [INF] * (n+1)
    graph = get_graph(n)
    solution(graph,distance,start)
    answer = get_answer(distance)
    print(answer)

def get_graph(n):
    graph = [[] for _ in range(n+1)]
    m = int(input())
    for _ in range(m):
        d,e,l = map(int,input().split())
        graph[d].append((e,l))
        graph[d].append((d,l))
    return graph

def solution(graph,distance,start):
    q = []
    for x in start:
        heapq.heappush(q,(0,x))
        distance[x] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

def get_answer(distance):
    answer = 1
    for i in range(1,n+1):
        if distance[answer] < distance[i]:
            answer = i
    return answer
    
if __name__ == "__main__":
    main()