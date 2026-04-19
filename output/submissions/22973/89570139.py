n = int(input())

if n < 0: n *= -1

if n % 2 == 0:
    print(-1)
else:
    answer = 0
    while True:
        if n == 0: break
        if n % 2 != 0: answer += 1
        n = n // 2
    print(answer)