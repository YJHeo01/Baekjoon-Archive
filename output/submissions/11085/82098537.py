import sys, heapq

input = sys.stdin.readline

def main():
    p,w = map(int,input().split())
    c,v = map(int,input().split())
    graph = [[] for _ in range(p)]
    for _ in range(w):
        start, end, width = map(int,input().split())
        graph[start].append((end,width))
        graph[end].append((start,width))
    max_width = [0] * p
    dijkstra(graph,max_width,c)
    print(max_width[v])

def dijkstra(graph,max_width,start):
    q = []
    max_width[start] = int(1e9)
    heapq.heappush(q,(-int(1e9),start))
    while q:
        width, vx = heapq.heappop(q)
        width *= -1
        if max_width[vx] > width:
            continue
        for nx, dw in graph[vx]:
            nw = min(width,dw)
            if nw > max_width[nx]:
                max_width[nx] = nw
                heapq.heappush(q,(-nw,nx))

if __name__ == "__main__":
    main()