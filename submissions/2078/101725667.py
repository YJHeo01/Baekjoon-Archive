a,b = map(int,input().split())

L,R = 0,0

while True:
    if a == 1 and b == 1: break
    if a > b:
        L += 1
        a -= b
    else:
        R += 1
        b -= a

print(L,R)