n,m = map(int,input().split())
if n >= m:
    print(0)
else:
    answer = 1
    for i in range(2,n+1):
        answer *= i
        answer %= m
        if answer == 0: break
    print(answer)