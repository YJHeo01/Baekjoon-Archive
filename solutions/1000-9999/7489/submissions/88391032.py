for _ in range(int(input())):
    answer = 1
    n = int(input())
    for i in range(2,n+1):
        answer *= i
        while True:
            if answer % 10 != 0: break
            answer //= 10
    answer %= 10
    print(answer)