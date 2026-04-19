n = int(input())

if n == 0:
    print("NO")
    exit(0)

tmp = 1

while True:
    if tmp >= n: break
    tmp *= 3
    
while True:
    if tmp == 0: break
    if n >= tmp:
        n -= tmp
    tmp //= 3
    
if n == 0:
    print("YES")
else:
    print("NO")