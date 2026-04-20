n = int(input())

card = list(map(int,input().split()))
card_num = [0] * 20000001
for i in card:
    card_num[i] += 1
m = int(input())
card_list = list(map(int,input().split()))
for i in card_list:
    print(card_num[i],end = ' ')