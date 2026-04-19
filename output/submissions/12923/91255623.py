import sys

input = sys.stdin.readline

n = int(input())

state = [-1] * n

stage = [[] for _ in range(2002)]

for i in range(n):
    a,b = map(int,input().split())
    stage[a].append((i,0))
    stage[b].append((i,1))
    
answer = 0

score = 0

while True:
    finish = True
    for i in range(score,-1,-1):
        stop = False
        while stage[i]:
            j,k = stage[i].pop()
            if state[j] >= k: continue
            score += (k-state[j])
            state[j] = k
            answer += 1
            stop = True
            finish = False
            break
        if stop: break
    if finish: break

for i in range(n):
    if state[i] != 1:
        print("Too Bad")
        exit(0)
        
print(answer)