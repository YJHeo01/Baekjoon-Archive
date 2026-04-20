import sys

input = sys.stdin.readline

meat_list = []

n,m = map(int,input().split())

for _ in range(n):
    weight,price = map(int,input().split())
    meat_list.append((price,weight))
meat_list.sort()
last_price = 0
same_price_weight_sum = 0
answer = -1
weight_sum = 0
for i in range(n):
    price,weight = meat_list[i]
    if last_price == price:
        weight_sum -= meat_list[i-1][1]
        same_price_weight_sum += meat_list[i-1][1]
    else:
        last_price = price
        weight_sum += same_price_weight_sum
        same_price_weight_sum = 0
    weight_sum += weight
    if weight_sum >= m:
        answer = price
        break

print(answer)