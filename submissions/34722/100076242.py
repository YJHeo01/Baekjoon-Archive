n = int(input())

answer = 0

for _ in range(n):
    tmp = 0
    s,c,a,r = map(int,input().split())
    if s >= 1000: tmp += 1
    if c >= 1600: tmp += 1
    if a >= 1500: tmp += 1
    if r >0 and r <= 30: tmp += 1
    if tmp != 0: answer += 1

print(answer)