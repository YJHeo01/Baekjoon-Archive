n = int(input())

answer = 7
tmp = 1
while True:
    answer += 1
    n -= tmp
    if n <= 0:
        break
    tmp *= 2

answer += 2

print(answer)