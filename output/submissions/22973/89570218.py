n = int(input())

if n < 0: n *= -1

if n % 2 == 0 and n != 0:
    print(-1)
else:
    answer = 0
    while True:
        if n == 0: break
        answer += 1
        n = n // 2
    print(answer)