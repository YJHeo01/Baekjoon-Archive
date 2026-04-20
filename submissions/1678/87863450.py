t,m,n = map(int,input().split())

train = []

train_cnt = 0

for _ in range(t):
    name, *tmp = input().split()
    tmp.pop()
    for i in tmp:
        train.append((int(i),name))
        train_cnt += 1

train.sort()

for i in range(train_cnt):
    if train[i][0] > m: break
    n += 1

n %= train_cnt

print(train[n][1])