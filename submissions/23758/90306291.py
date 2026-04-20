import sys, heapq

input = sys.stdin.readline

n = int(input())

array = sorted(list(map(int,input().split())))

q = []

for i in range(n//2+n%2):
    heapq.heappush(q,-array[i])

    answer = 0

while q:
    value = heapq.heappop(q)
    value *= -1
    answer += 1
    value //= 2
    if value == 0: break
    heapq.heappush(q,-value)

print(answer)