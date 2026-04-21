from collections import deque

n = int(input())

card = [0] * n

for i in range(n):
    card[i] = i+1

card = deque(card)

while 1:
    card.popleft()
    v = card.popleft()
    card.append(v)
    if len(card) == 1:
        print(card[0])
        break
