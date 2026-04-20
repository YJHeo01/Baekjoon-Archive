import heapq
import sys

input = sys.stdin.readline

n = int(input())
quiz = [[] for _ in range(n+1)]

for _ in range(n):
    deadline, ramen = map(int,input().split())
    heapq.heappush(quiz[deadline],-ramen)

answer = 0

for i in range(n+1):
    if quiz[i] == []:
        continue
    answer -= heapq.heappop(quiz[i])

print(answer)