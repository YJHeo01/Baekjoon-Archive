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
for i in range(n):
    price,weight = meat_list[i]
    sum_meat += weight
    if last_price != price:
        if sum_meat >= m:
            answer = price
            break

print(answer)