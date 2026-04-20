n = int(input())

fruit = list(map(int,input().split()))

left,right = 0,0

answer = 0

joker = 0

tmp = 0

while right < n:
    answer = max(answer,right-left + 1)
    if fruit[left] != fruit[right]:
        if joker == 0:
            if right + 1 < n and fruit[left] == fruit[right+1]:
                joker = 1
                right += 1
            else:
                left = right
        else:
            left = right
            joker = 0
    else:
        right += 1

print(answer)