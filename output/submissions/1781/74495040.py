import sys,heapq

input = sys.stdin.readline

n = int(input())

prior_q = []

for _ in range(n):
    a,b = map(int,input().split()) 
    heapq.heappush(prior_q,(a,-b))

answer = 0

time = 1

while prior_q:
    deadline, cnt = heapq.heappop(prior_q)
    cnt *= -1
    if deadline >= time:
        answer += cnt
        time += 1

print(answer)