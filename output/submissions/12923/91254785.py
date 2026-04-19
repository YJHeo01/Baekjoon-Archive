import sys

input = sys.stdin.readline

n = int(input())

finish = [-1] * n

stage = [[] for _ in range(2002)]

for i in range(n):
    a,b = map(int,input().split())
    stage[b].append((i,1))
    stage[a].append((i,0))
    
answer = 0

last_score = -1
score = 0

while True:
    next_score = score
    if last_score == score: break
    for i in range(score,last_score,-1):
        stop = False
        for j,k in stage[i]:
            if finish[j] >= k: continue
            next_score += (k-finish[j])
            finish[j] = k
            answer += 1
            stop = True
            break
        if stop: break
    last_score = score
    score = next_score

for i in range(n):
    if finish[i] != 1:
        print("Too Bad")
        exit(0)
        
print(answer)
            