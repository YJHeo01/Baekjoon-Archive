import sys, heapq

input = sys.stdin.readline

def main():
    global k
    n,m,k,s,t = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    reverse_graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,ti = map(int,input().split())
        graph[a].append((b,ti))
        reverse_graph[b].append(a)
    time_table = [[-1]*(k+1) for _ in range(n+1)]
    solution(graph,reverse_graph,time_table,s)
    print(time_table[t][k])

def solution(graph,reverse_graph,time_table,s):
    q = []
    time_table[s][0] = 0
    heapq.heappush(q,(0,s,0))
    while q:
        time, vx, cnt = heapq.heappop(q)
        time *= -1
        if time_table[vx][cnt] > time:
            continue
        for nx,dt in graph[vx]:
            nt = time + dt
            if nt > time_table[nx][cnt]:
                time_table[nx][cnt] = nt
                heapq.heappush(q,(-nt,nx,cnt))
        if cnt == k: continue
        for nx in reverse_graph[vx]:
            if time > time_table[nx][cnt+1]:
                time_table[nx][cnt+1] = time
                heapq.heappush(q,(-time,nx,cnt+1))

if __name__ == "__main__":
    main()