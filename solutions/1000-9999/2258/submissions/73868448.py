import sys

input = sys.stdin.readline

n,m = map(int,input().split())

meat_list = []

for _ in range(n):
    weight,price = map(int,input().split())
    meat_list.append((price,weight))

meat_list = sorted(meat_list,key=lambda x:(x[0],-x[1]))

last_price = 0
sum_meat = 0
answer = -1
same_price_cnt = 1
for i in range(n):
    price,weight = meat_list[i]
    sum_meat += weight
    if last_price != price:
        same_price_cnt = 1
    else:
        same_price_cnt += 1
    if sum_meat >= m:
        if answer == -1:
            answer = price * same_price_cnt
        else:
            answer = min(answer,answer = price * same_price_cnt)
    last_price = price

print(answer)