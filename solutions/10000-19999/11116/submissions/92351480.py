import heapq

n = int(input())

for _ in range(n):
    m = int(input())
    visited = [[False]*2 for _ in range(m)]
    left = list(map(int,input().split()))
    right = list(map(int,input().split()))
    q = []
    for i in range(m):
        heapq.heappush(q,(left[i],i,0))
        heapq.heappush(q,(right[i],i,1))
    answer = 0
    while q:
        time, idx, state = heapq.heappop(q)
        if visited[idx][state]: continue
        if state == 0:
            answer += 1
            for i in range(m):
                if left[i] == time + 500:
                    visited[i][0] = True
                    break
            for i in range(m):
                if right[i] == time + 1000:
                    visited[i][1] = True
                    break
            for i in range(m):
                if right[i] == time + 1500:
                    visited[i][1] = True
                    break
        else:
            for i in range(m):
                if right[i] == time + 500:
                    visited[i][1] = True
                    break
            for i in range(m):
                if left[i] == time + 1000:
                    visited[i][0] = True
                    break
            for i in range(m):
                if left[i] == time + 1500:
                    visited[i][0] = True
                    break
    print(answer)