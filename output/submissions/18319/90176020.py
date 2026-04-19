import heapq

n,k = map(int,input().split())

array = sorted(list(map(int,input().split())))

array.reverse()

for _ in range(n-k): array.pop()

cnt = [1] * k

max_heap = []
min_heap = []

for i in range(k):
    heapq.heappush(max_heap,(-array[i],-1,i))
    heapq.heappush(min_heap,(array[i],-1,i))
    
while max_heap:
    max_value, max_div, max_idx = heapq.heappop(max_heap)
    max_div *= -1
    if cnt[max_idx] != max_div: continue
    max_value *= -1
    while min_heap:
        min_value, min_div, min_idx = heapq.heappop(min_heap)
        if cnt[min_div] == -min_div: break
    min_div *= -1
    new_value = array[max_idx] // (max_div+1)
    if new_value < min_value or max_idx == min_idx: 
        heapq.heappush(max_heap,(-max_value,-max_div,max_idx))
        break
    cnt[max_idx] += 1
    for _ in range(array[max_idx]%cnt[max_idx]):
        heapq.heappush(max_heap,(-(new_value+1),-(max_div+1),max_idx))
        heapq.heappush(min_heap,((new_value+1),-(max_div+1),max_idx))
    for _ in range(array[max_idx]%cnt[max_idx],cnt[max_idx]):
        heapq.heappush(max_heap,(-new_value,-(max_div+1),max_idx))
        heapq.heappush(min_heap,(new_value,-(max_div+1),max_idx))

answer = 0

for _ in range(k//2):
    while max_heap:
        value, div, idx = heapq.heappop(max_heap)
        if cnt[idx] != -div: continue
        break

for _ in range(k//2):
    while max_heap:
        value, div, idx = heapq.heappop(max_heap)
        if cnt[idx] != -div: continue
        answer -= value
        break



print(answer)