import sys, heapq

input = sys.stdin.readline

n = int(input())

contest = []

for _ in range(n):
    contest.append(list(map(int,input().split())))

money = []

cant_join_cnt = 0

sum_money = 0

for x,p in contest:
    if sum_money > x:
        while money:
            tmp = heapq.heappop(money)
            sum_money += tmp
            cant_join_cnt += 1
            if sum_money <= x: break
    sum_money += p
    heapq.heappush(money,-p)

if cant_join_cnt > 1:
    print("Zzz")
else:
    print("Kkeo-eok")