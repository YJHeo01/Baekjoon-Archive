n = int(input())
n = 1000 - n
answer = 0
coin_list = [500,100,50,10,5,1]

for coin in coin_list:
    answer += n // coin
    n %= coin

print(answer)