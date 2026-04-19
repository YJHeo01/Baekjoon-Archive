input()

HI_ARC = {'H','I','A','R','C'}

cnt = {}

for c in HI_ARC: cnt[c] = 0

for i in input():
    if i in HI_ARC:
        cnt[i] += 1

answer = 100000

for c in cnt:
    answer = min(answer,cnt[c])
    
print(answer)