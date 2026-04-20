import sys
input = sys.stdin.readline
n = int(input())
card_list = []
for i in range(n):
    card = int(input())
    card_list.append(card)
card_list.sort()
sum = 0
if n > 1:
    sum = card_list[0] + card_list[1]
    for i in range(2,n):
        sum += (sum + card_list[i])
else:
    sum = card_list[0]
print(sum)
