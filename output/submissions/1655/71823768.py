import heapq

n = int(input())
mid_value = int(input())
large_heap = []
small_heap = []
print(mid_value)
for i in range(n-1):
    tmp = int(input())
    if i % 2 == 0:
        if tmp > mid_value:
            heapq.heappush(large_heap,tmp)
        else:
            heapq.heappush(large_heap,mid_value)
            heapq.heappush(small_heap,-tmp)
            mid_value = -heapq.heappop(small_heap)
    else:
        if tmp < mid_value:
            heapq.heappush(small_heap,-tmp)
        else:
            heapq.heappush(small_heap,-mid_value)
            heapq.heappush(large_heap,tmp)
            mid_value = heapq.heappop(large_heap)
    print(mid_value)