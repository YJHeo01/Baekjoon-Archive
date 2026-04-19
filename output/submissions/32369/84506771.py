n,a,b = map(int,input().split())

x,y = 1,1

for i in range(n):
    x += a; y += b
    if x == y:
        y -= 1
    if x < y: x,y = y,x

print(x,y)