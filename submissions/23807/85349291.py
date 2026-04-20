import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    x,z = map(int,input().split())
    p = int(input())
    y = list(map(int,input().split()))
    mid = [False] * (n+1)
    for i in y:
        mid[i] = True
    INF = int(1e12)
    distance = [[INF]*4 for _ in range(n+1)]
    solution(graph,distance,x,mid)
    answer = distance[z][3]
    if answer >= INF:
        answer = -1
    print(answer)

def solution(graph,distance,start,mid):
    q = []
    heapq.heappush(q,(0,0,set([]),start))
    distance[start][0] = 0
    while q:
        dist, mid_cnt, mid_list, vx = heapq.heappop(q)
        if dist > distance[vx][mid_cnt]: continue
        for nx,w in graph[vx]:
            next_mid_list = mid_list.union(set([nx]))
            if (mid_cnt == 3 and nx not in mid_list) or mid[nx] == False:
                next_mid_list.remove(nx)
            next_mid_cnt = len(next_mid_list)
            next_dist = dist + w
            if distance[nx][next_mid_cnt] > next_dist:
                distance[nx][next_mid_cnt] = next_dist
                heapq.heappush(q,(next_dist,next_mid_cnt,next_mid_list,nx))

if __name__ == "__main__":
    main()