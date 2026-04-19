t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    u = 0
    while True:
        if m * 2 == n: break
        u += 1
        n -= 1
        m -= 1
    print(u,n//2)