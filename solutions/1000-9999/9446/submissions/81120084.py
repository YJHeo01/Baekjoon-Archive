import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    cost = [0] + list(map(int,input().split()))
    recipe = [[] for _ in range(n+1)]
    q = []
    for _ in range(m):
        a,x,y = map(int,input().split())
        recipe[x].append((a,y))
    for i in range(1,n+1):
        heapq.heappush(q,(cost[i],i))
    while q:
        value, vx = heapq.heappop(q)
        if value > cost[vx]: continue
        for nx, tmp in recipe[vx]:
            if cost[nx] > value + cost[tmp]:
                cost[nx] = value + cost[tmp]
                heapq.heappush(q,(cost[nx],nx))
    print(cost[1])
        
if __name__ == "__main__":
    main()