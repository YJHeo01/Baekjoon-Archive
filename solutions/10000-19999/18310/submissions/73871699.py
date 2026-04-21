n = int(input())

house = list(map(int,input().split()))

answer = 0

mid = sum(house) / n

for x in house:
    if abs(answer-mid) > abs(x - mid):
        answer = x
    elif abs(answer-mid) == abs(x - mid) and x < answer:
        answer = x
    else:
        continue

print(answer)
