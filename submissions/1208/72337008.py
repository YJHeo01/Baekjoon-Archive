import heapq

n,s = map(int,input().split())

array = list(map(int,input().split()))

array.sort()

num_list = []

for i in range(n):
    heapq.heappush(num_list,(i,array[i]))

answer = 0
while num_list != []:
    idx, value = heapq.heappop(num_list)
    idx += 1
    if idx == n:
        if value == s:
            answer += 1
        continue
    if value > s:
        continue
    heapq.heappush(num_list,(idx,value))
    if value + array[idx] <= s:
        heapq.heappush(num_list,(idx,value+array[idx]))

print(answer)