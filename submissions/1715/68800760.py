import sys
input = sys.stdin.readline
n = int(input())
card_list = []
for i in range(n):
    card = int(input())
    card_list.append(card)
card_list.sort(reverse=True)

sum = 0

cnt = 1

for i in card_list:
    sum += i * cnt
    cnt += 1
if len(card_list) > 1:
    sum -= card_list[-1]
print(sum)