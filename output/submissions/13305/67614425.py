n = int(input())

distance = list(map(int,input().split()))

city = list(map(int, input().split()))

best_price_index = 0

answer = 0
for i in range(n-1):
    if city[i] <= city[best_price_index]:
        best_price_index = i
    answer += distance[i]*city[best_price_index]

print(answer)