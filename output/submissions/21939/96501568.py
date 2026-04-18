import sys, heapq

input = sys.stdin.readline

n = int(input())

problems = [-1] * 100001

min_heap = []

max_heap = []

for _ in range(n):
    p,l = map(int,input().split())
    problems[p] = l
    heapq.heappush(min_heap,(l,p))
    heapq.heappush(max_heap,(-l,-p))
    
m = int(input())

for _ in range(m):
    tmp = list(input().split())
    if tmp[0] == 'recommend':
        x = int(tmp[1])
        if x == 1:
            while True:
                l,p = heapq.heappop(max_heap)
                l *= -1; p *= -1
                if problems[p] != l: continue
                print(p)
                heapq.heappush(max_heap,(-l,-p))
                break
        else:
            while True:
                l,p = heapq.heappop(min_heap)
                if problems[p] != l: continue
                print(p)
                heapq.heappush(min_heap,(l,p))
                break
    elif tmp[0] == "solved":
        p = int(tmp[1])
        problems[p] = -1
    else:
        p,l = int(tmp[1]), int(tmp[2])
        problems[p] = l
        heapq.heappush(max_heap,(-l,-p))
        heapq.heappush(min_heap,(l,p))