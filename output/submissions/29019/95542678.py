while True:
    y,c,r = map(int,input().split())
    if y == 0 and c == 0 and r == 0: break
    answer = y * c
    left, right = 0, answer
    while left <= right:
        mid = (left+right) // 2
        money = mid
        for _ in range(y):
            money -= c
            if money < 0: break
            money += money * (r) // 100
        if money >= 0:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)