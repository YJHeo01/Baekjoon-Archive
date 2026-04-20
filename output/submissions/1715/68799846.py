import sys
input = sys.stdin.readline
n = int(input())
card_list = []
for i in range(n):
    card = int(input())
    card_list.append(card)
card_list.sort()
sum = 0
l = n
while 1:
    new_card_list = []
    if l == 1:
        if sum == 0:
            sum = card_list[0]
            break
        else:
            break
    for i in range(0,l-1,2):
        tmp = card_list[i] + card_list[i+1]
        new_card_list.append(tmp)
        sum += tmp
    if l % 2 == 1:
        new_card_list.append(card_list[l-1])
        new_card_list.sort()
    l = len(new_card_list)
    card_list = new_card_list

print(sum)