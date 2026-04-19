a,b,c,m = map(int,input().split())
tired = 0
answer = 0
for _ in range(24):
    if tired + a <= m:
        tired += a
        answer += b
    else:
        tired -= c
    if tired < 0:
        tired = 0
print(answer)