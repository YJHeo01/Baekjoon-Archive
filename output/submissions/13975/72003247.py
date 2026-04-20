import heapq

t = int(input())

for _ in range(t):
    k = int(input()) - 1
    file_list = list(map(int,input().split()))
    heapq.heapify(file_list)
    answer = 0
    for _ in range(k):
        value = heapq.heappop(file_list) +  heapq.heappop(file_list)
        answer += value
        heapq.heappush(file_list,value)
    print(answer)