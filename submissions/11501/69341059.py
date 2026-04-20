t = int(input())

for _ in range(t):
    n = int(input())
    stocks = list(map(int,input().split()))
    answer = 0
    buy_start_day = 0
    while buy_start_day < n:
        max_val = 0
        max_val_idx = buy_start_day
        for i in range(buy_start_day,n):
            if stocks[i] >= max_val:
                max_val_idx = i
                max_val = stocks[i]
        answer += (max_val * (max_val_idx - buy_start_day) - sum(stocks[buy_start_day:max_val_idx]))
        buy_start_day = max_val_idx + 1
    print(answer)