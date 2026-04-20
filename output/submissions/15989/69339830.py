t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    three = n // 3
    for i in range(three+1):
        tmp = n - i*3
        two = tmp // 2
        for j in range(two+1):
            cnt += 1

    print(cnt)