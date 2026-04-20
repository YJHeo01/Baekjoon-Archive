n,r,c = map(int,input().split())
x, y = 0,0
cnt = 0
while(n):
    if c >= 2 ** (n-1) + x:
        cnt += 4**(n-1)
        x += 2 ** (n-1)
    if r >= 2 ** (n-1) + y:
        cnt += 2 * (4**(n-1))
        y+= 2 ** (n-1)
    n -= 1

print(cnt)