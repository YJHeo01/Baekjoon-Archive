import sys,heapq

input = sys.stdin.readline

n = int(input())

prior_q = []

time = 0

for _ in range(n):
    ramen_cnt,deadline = map(int,input().split())
    heapq.heappush(prior_q,(ramen_cnt,-deadline))

answer = 0

while prior_q:
    ramen_cnt,deadline = heapq.heappop(prior_q)
    deadline *= -1
    if time < ramen_cnt:
        time +=1
        answer += deadline

print(answer)
