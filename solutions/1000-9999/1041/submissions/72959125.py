n = int(input())

dice_list = list(map(int,input().split()))

dice_list.sort()

answer = 0

if n == 1:
    answer = sum(dice_list[:5])
else:
    answer = 4 * dice_list[2] + (8 + 8*(n-2)) * dice_list[1] + (5 * (n**2) - 12 - 8*(n-2)) * dice_list[0]

print(answer)