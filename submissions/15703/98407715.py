n = int(input())

dice = list(map(int,input().split()))

dice.sort()

answer = n

left = 1
right = n

while left <= right:
    mid = (left+right)//2
    possible = True
    for i in range(n):
        if dice[i] < i // mid:
            possible = False
    if possible:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)