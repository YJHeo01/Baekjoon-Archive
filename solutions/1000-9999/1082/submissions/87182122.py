n = int(input())

price = list(map(int,input().split()))

m = int(input())

min_price = min(price[1:])
min_price_num = -1

for i in range(n-1,0,-1):
    if min_price == price[i]:
        min_price_num = i
        break

if min_price > m:
    print(0)
    exit(0)

answer = []

answer.append(min_price_num)

m -= min_price

min_price = min(price)

for i in range(n-1,-1,-1):
    if min_price == price[i]:
        min_price_num = i
        break

digit = 1

while True:
    if min_price > m:
        break
    digit += 1
    m -= min_price
    answer.append(min_price_num)

for i in range(digit):
    for num in range(n-1,0,-1):
        if answer[i] >= num or m >= price[num] - price[answer[i]]: 
            m -= (price[num] - price[answer[i]])
            answer[i] = num
            break

for i in answer:
    print(i,end="")