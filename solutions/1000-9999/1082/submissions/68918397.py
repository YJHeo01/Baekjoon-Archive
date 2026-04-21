n = int(input())
price = list(map(int,input().split()))
m = int(input())
min_value = min(price)
l = m // min_value
tmp = m % min_value
answer = 0
for i in range(n-1,-1,-1):
    if tmp > (price[i] - min_value):
        answer += i
        tmp -= (price[i] - min_value)
        break

cnt = 0
if answer == 0:
    print(0)
else:
    for i in range(l-1):
        for j in range(n-1,-1,-1):
            if tmp >= (price[j] - min_value):
                answer *= 10
                answer += j
                tmp -= (price[j] - min_value)
                break
            if j == 0:
                cnt += 1
    for i in range(n):
        if price[i] == min_value:
            min_value = i
            break
    for i in range(cnt):
        answer *= 10
        answer+= min_value
    print(answer)