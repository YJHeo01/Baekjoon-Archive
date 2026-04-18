import sys, heapq

input = sys.stdin.readline

n,T,k = map(int,input().split())

answer = 0

q = []

for _ in range(n):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        t,f = tmp[1:]
        while q:
            a,b = heapq.heappop(q)
            if (t - b) > T: continue
            heapq.heappush(q,(a,b))
            break
        heapq.heappush(q,(-f,t))
    else:
        t = tmp[1]
        for _ in range(k):
            while q:
                a,b = heapq.heappop(q)
                if (t - b) > T: continue
                answer -= a
                break
    
print(answer)