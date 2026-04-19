import heapq

n,k = map(int,input().split())

array = list(map(int,input().split()))

score_list = []

tmp = 0

for i in array:
    tmp += i
    heapq.heappush(score_list,-tmp)
    
answer = 0

for _ in range(k):
    answer -= heapq.heappop(score_list)

print(answer)