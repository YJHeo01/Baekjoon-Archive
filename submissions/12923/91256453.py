import sys, heapq

input = sys.stdin.readline

n = int(input())

state = [-1] * n

q_a = []
q_b = []

answer = 0

score = 0

a_list = [[] for _ in range(2003)]

for i in range(n):
    a,b = map(int,input().split())
    if b == 0:
        state[i] = 1
        answer += 1
        score += 2
        continue
    heapq.heappush(q_b,(b,i))
    if a == 0:
        heapq.heappush(q_a,(-b,i))
    a_list[a].append((-b,i))
    

while True:
    last_score = score
    while q_b:
        need_score, idx = heapq.heappop(q_b)
        if need_score > score:
            heapq.heappush(q_b,(need_score,idx))
            break
        else:
            answer += 1
            score += (1 - state[idx])
            state[idx] = 1
    while q_a:
        tmp, idx = heapq.heappop(q_a)
        if state[idx] >= 0: continue
        answer += 1
        score += 1
        state[idx] = 0
        break
    if last_score == score: break
    for i in range(last_score,score+1):
        for tmp in a_list[i]:
            heapq.heappush(q_a,tmp)

for i in range(n):
    if state[i] != 1:
        print("Too Bad")
        exit(0)
        
print(answer)