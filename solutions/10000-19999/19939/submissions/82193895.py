n,k = map(int,input().split())

n -= k*(k+1) // 2

if n < 0:
    print(-1)
    exit(0)

while True:
    if n < k:
        break
    n -= k

if n == 0:
    k -= 1

print(k)