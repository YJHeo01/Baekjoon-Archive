import heapq
import sys
input = sys.stdin.readline
T = int(input())
max_heap = []
min_heap = []
for i in range(T):
    last_i = 0
    t = int(input())
    for j in range(t):
        command, n = input().split()
        n = int(n)
        if command == 'I':
            heapq.heappush(min_heap,n)
            heapq.heappush(max_heap,-n)
            last_i+=1
        else:
            if last_i == 0:
                min_heap = []
                max_heap = []
            else:
                last_i-=1
                if n == 1:
                    heapq.heappop(max_heap)
                else:
                    heapq.heappop(min_heap)
    if last_i == 0:
        print("EMPTY")
    else:
        print(-(heapq.heappop(max_heap)),heapq.heappop(min_heap))