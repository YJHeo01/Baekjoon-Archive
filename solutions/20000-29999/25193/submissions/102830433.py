n = int(input())
S = list(input())
c = 0

for i in S:
    if i == 'C': c += 1

left = 0
right = n

answer = n

while left <= right:
    mid = (left+right) // 2
    food = n
    chicken = c
    combo = 0
    success = True
    for _ in range(n):
        if combo == mid:
            if food == chicken:
                success = False
                break
            combo = 0
            food -= 1
        else:
            food -= 1
            combo += 1
            chicken -= 1
    if success:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)