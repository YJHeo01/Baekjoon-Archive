import sys, heapq

input = sys.stdin.readline

def main():
    global k
    n,m,k,s,T = map(int,input().split())
    ski = [[] for _ in range(n+1)]
    lift = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,t = map(int,input().split())
        ski[a].append((b,t))
        lift[b].append(a)
    time = [[-1]*(k+1) for _ in range(n+1)]
    solution(ski,lift,time,s)
    print(max(time[T]))

def solution(ski,lift,time,start):
    q = []
    time[start][0] = 0
    heapq.heappush(q,(0,0,start))
    while q:
        vt, cnt, vx = heapq.heappop(q)
        vt *= -1
        if vt < time[vx][cnt]: continue
        for nx, dt in ski[vx]:
            nt = vt + dt
            if nt > time[nx][cnt]:
                time[nx][cnt] = nt
                heapq.heappush(q,(-nt,cnt,nx))
        if cnt == k: continue
        for nx in lift[vx]:
            if vt > time[nx][cnt+1]:
                time[nx][cnt+1] = vt
                heapq.heappush(q,(-vt,cnt+1,nx))

if __name__ == "__main__":
    main()