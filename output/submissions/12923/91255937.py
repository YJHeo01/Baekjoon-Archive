import sys, heapq

input = sys.stdin.readline

n = int(input())

state = [-1] * n

q_a = []
q_b = []

for i in range(n):
    a,b = map(int,input().split())
    heapq.heappush(q_b,(b,i))
    heapq.heappush(q_a,(a,i))
    
answer = 0

score = 0

while True:
    finish = True
    last_score = score
    while q_b:
        need_score, idx = heapq.heappop(q_b)
        if need_score > score:
            heapq.heappush(q_b,(need_score,idx))
            break
        else:
            answer += 1
            score += 1 - state[idx]
            state[idx] = 1
    while q_a:
        need_score, idx = heapq.heappop(q_a)
        if state[idx] == 1: continue
        if score >= need_score:
            answer += 1
            score += 1
            state[idx] = 0
        else:
            heapq.heappush(q_a,(need_score,idx))
        break
    if last_score == score: break

for i in range(n):
    if state[i] != 1:
        print("Too Bad")
        exit(0)
        
print(answer)