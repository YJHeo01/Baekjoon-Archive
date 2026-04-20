import heapq
import sys

input = sys.stdin.readline

n = int(input())

quiz = []
solve_list = [0]*(n+1)
for _ in range(n):
    deadline, ramen = map(int,input().split())
    heapq.heappush(quiz,(-deadline,-ramen))
answer = 0
minimum = 0
last_deadline = n
same_deadline_cnt = 0
while quiz:
    deadline,ramen = heapq.heappop(quiz)
    deadline,ramen = -deadline,-ramen
    if last_deadline == deadline:
        same_deadline_cnt += 1
    else:
        same_deadline_cnt = 0
    deadline -= same_deadline_cnt
    for i in range(deadline,0,-1):
        if ramen > solve_list[i]:
            solve_list = solve_list[1:i+1] + [ramen] + solve_list[i+1:] #틀릴 경우 첫째 항 가장 작은 값 idx 찾기
            break

print(sum(solve_list[1:]))