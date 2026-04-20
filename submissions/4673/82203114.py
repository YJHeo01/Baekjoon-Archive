INF = 10001

self_number = [True] * INF

for i in range(1,INF):
    target = i
    while True:
        if i == 0:
            break
        target += i % 10
        i = i // 10
    if target >= INF:
        continue
    self_number[target] = False

for i in range(1,INF):
    if self_number[i] == True:
        print(i)