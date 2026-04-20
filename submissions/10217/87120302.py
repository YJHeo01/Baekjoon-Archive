import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        global n,m
        n,m,k = map(int,input().split())
        graph = [[] for _ in range(n+1)]
        for _ in range(k):
            u,v,c,d = map(int,input().split())
            graph[u].append((c,d,v))
            graph[v].append((c,d,u))
        distance = [[INF]*(m+1) for _ in range(n+1)]
        shortest_paht(graph,distance)
        answer = min(distance[n])
        if answer >= INF:
            print("Poor KCM")
        else:
            print(answer)

def shortest_paht(graph,time):
    time[1][0] = 0
    for vc in range(m):
        for vx in range(1,n+1):
            if time[vx][vc] >= INF: continue
            vt = time[vx][vc]
            for dc, dt, nx in graph[vx]:
                nc = vc + dc
                if nc > m: continue
                nt = vt + dt
                if time[nx][nc] > nt:
                    time[nx][nc] = nt

if __name__ == "__main__":
    INF = int(1e9)
    main()