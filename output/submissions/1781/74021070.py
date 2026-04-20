import sys,heapq

input = sys.stdin.readline

n = int(input())

prior_q = []

time = 0

for _ in range(n):
    deadline,ramen_cnt = map(int,input().split())
    heapq.heappush(prior_q,(deadline,-ramen_cnt))

answer = 0

while prior_q:
    deadline,ramen_cnt = heapq.heappop(prior_q)
    ramen_cnt *= -1
    if time < deadline:
        time +=1
        answer += ramen_cnt

print(answer)