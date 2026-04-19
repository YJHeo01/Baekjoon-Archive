r,k,m = map(int,input().split())

idx = 1
while True:
    m -= k
    if r == 0 or m < 0: break
    r //= 2
    

print(r)