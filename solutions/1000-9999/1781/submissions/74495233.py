import sys,heapq

input = sys.stdin.readline

n = int(input())

prior_q = []

for _ in range(n):
    a,b = map(int,input().split()) 
    heapq.heappush(prior_q,(-a,-b))

answer = 0

time = n

while prior_q:
    deadline, cnt = heapq.heappop(prior_q)
    deadline *= -1; cnt *= -1
    if deadline > time:
        continue
    answer += cnt
    time = deadline - 1

print(answer)