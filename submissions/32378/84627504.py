import sys, heapq

input = sys.stdin.readline

def main():
    n,k,s = map(int,input().split())
    if k >= 37:
        print("MEGA")
        return
    array = list(map(int,input().split()))
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = s
    q = []
    heapq.heappush(q,(-s,0,0))
    while q:
        vd, vx, vy = heapq.heappop(q)
        vd *= -1
        if dp[vx][vy] > vd or dp[vx][vy] <= 0 or vx == n: continue
        nd,nx,ny = vd + array[vx],vx + 1, vy
        if nd > dp[nx][ny]:
            dp[nx][ny] = nd
            heapq.heappush(q,(-nd,nx,ny))
        if vy == k : continue
        nd,nx,ny = vd * 2, vx + 1, vy + 1
        if nd > dp[nx][ny]:
            dp[nx][ny] = nd
            heapq.heappush(q,(-nd,nx,ny))


    answer = max(dp[n])
    if answer > 10 ** 11:
        print("MEGA")
    elif answer <= 0:
        print("-1")
    else:
        print(answer)


if __name__ == "__main__":
    main()