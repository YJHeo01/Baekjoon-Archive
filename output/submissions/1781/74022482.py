import sys,heapq

input = sys.stdin.readline

n = int(input())

prior_q = []

time = n

for _ in range(n):
    deadline,ramen_cnt = map(int,input().split())
    heapq.heappush(prior_q,(-deadline,-ramen_cnt))

answer = 0
get_ramen_list = [0] * (n+1)

last_deadline = n+1
while prior_q:
    deadline,ramen_cnt = heapq.heappop(prior_q)
    deadline *= -1; ramen_cnt *= -1
    if last_deadline == deadline:
        time -= 1
    else:
        time = deadline
    last_deadline = deadline
    if time <= 0:
        continue
    if ramen_cnt > get_ramen_list[time]:
        answer -= get_ramen_list[time]
        answer += ramen_cnt
        get_ramen_list[time] = ramen_cnt
print(answer)

