import heapq
import sys

input = sys.stdin.readline

n = int(input())

quiz = []
solve_list = [0]*(n+1)
for _ in range(n):
    deadline, ramen = map(int,input().split())
    heapq.heappush(quiz,(-ramen,-deadline))

while quiz:
    ramen, deadline = heapq.heappop(quiz)
    ramen, deadline = -ramen,-deadline
    for i in range(deadline,0,-1):
        if solve_list[i] == 0:
            solve_list[i] = ramen
            break

print(sum(solve_list))