#https://github.com/YJHeo01

n,m = map(int,input().split())
money_day = []
for _ in range(n):
    money_day.append(int(input()))

left = min(money_day)
right = sum(money_day)
max_money = max(money_day)
k = int(1e9)

while left <= right:
    mid = (left + right) // 2
    tmp = mid
    find_money_cnt = 1
    if mid < max_money:
        left = mid + 1
        continue
    for money in money_day:
        if money > tmp:
            find_money_cnt += 1
            tmp = mid
        else:
            tmp -= money
    if find_money_cnt <= m:
        k = mid
        right = mid -1
    else:
        left = mid + 1

print(k)