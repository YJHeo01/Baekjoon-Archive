money = list(map(int,input().split()))

answer = 0

n = int(input())

for _ in range(n):
    tmp = list(input().split())
    if float(tmp[1]) >= 2.0 and int(tmp[2]) >= 17:
        answer += money[int(tmp[0])]

print(answer)