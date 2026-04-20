from itertools import combinations

n = int(input())

card_list = list(map(int,input().split()))

score_list = [0] * n

data = []

for i in range(n):
    data.append(i)

all_game = list(combinations(data,2))

for game in all_game:
    a = game[0]
    b = game[1]
    if card_list[a] % card_list[b] == 0:
        score_list[b] += 1
        score_list[a] -= 1
    elif card_list[b] % card_list[a] == 0:
        score_list[a] += 1
        score_list[b] -= 1
    else:
        continue

for score in score_list:
    print(score,end=" ")