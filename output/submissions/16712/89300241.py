n,m = map(int,input().split())

array = list(map(int,input().split())) + [int(1e9)]

score = []

for i in range(m):
    score.append(array[i])
    
order = list(map(int,input().split()))

idx = m

for c in order:
    score.sort()
    score[c-1] = array[idx]
    idx += 1
    
score.sort()
score.pop()

print(*score)