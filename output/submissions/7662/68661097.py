import heapq
import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    max_heap = []
    min_heap = []
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
                    v = heapq.heappop(max_heap)
                    l = len(min_heap)
                    for i in range(l):
                        if -v == min_heap[i]:
                            min_heap[i] = 2 ** 31
                            break   
                else:
                   v = heapq.heappop(min_heap)
                   l = len(max_heap)
                   for i in range(l):
                    if -v == max_heap[i]:
                        max_heap[i] = 2 ** 31
                        break
    if last_i == 0:
        print("EMPTY")
    else:
        print(-(heapq.heappop(max_heap)),heapq.heappop(min_heap))