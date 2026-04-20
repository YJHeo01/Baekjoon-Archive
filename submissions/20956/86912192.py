import heapq

n,m = map(int,input().split())
array = list(map(int,input().split()))
left_q, right_q = [], []

for i in range(n):
    heapq.heappush(left_q,(-array[i],i))
    heapq.heappush(right_q,(-array[i],-i))

eat = [False] * n
state = 'L'

for _ in range(m):
    if state == 'L':
        while True:
            amount, idx = heapq.heappop(left_q)
            if eat[idx] == False: break
    else:
        while True:
            amount, idx = heapq.heappop(right_q)
            idx *= -1
            if eat[idx] == False: break
    print(idx+1)
    eat[idx] = True
    if amount % 7 == 0:
        if state == 'L': state = 'R'
        else: state = 'L'