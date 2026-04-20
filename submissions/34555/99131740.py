n = int(input())

ans = []

x = n // 2 + n % 2

dx = 1

while True:
    if x <= 0 or x > n: break
    ans.append(x)
    if dx % 2 == 1:
        x += dx
    else:
        x -= dx
    dx+=1

print(*ans)

