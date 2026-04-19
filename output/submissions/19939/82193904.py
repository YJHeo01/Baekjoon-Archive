n,k = map(int,input().split())

n -= k*(k+1) // 2

if n < 0:
    print(-1)
    exit(0)

n %= k

if n == 0:
    k -= 1

print(k)