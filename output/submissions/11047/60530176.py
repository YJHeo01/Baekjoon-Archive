n,k = map(int,input().split())

coin_list = []

for i in range(n):
    tmp = int(input())
    coin_list.append(tmp)

coin_list.reverse()
cnt = 0
for coin in coin_list:
    cnt += (k // coin)
    k = k % coin
    if k == 0 : break

print(cnt)