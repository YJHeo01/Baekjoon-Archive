from collections import deque

n, k = map(int,input().split())

INF = 2*max(n,k)+1
point = [INF] * (INF)

point[n] = 0

time_answer = 200000
cnt_answer = 0

queue = deque([n])

dx = [-1,1,0]
while queue:
    v = queue.popleft()
    for i in range(3):
        if i != 2:
            nx = v + dx[i]
        else:
            nx = 2*v
        if nx < 0 or nx >= INF:
            continue
        if point[nx] >= point[v] + 1:
            point[nx] = point[v] + 1
            if nx == k:
                if point[nx] <= time_answer:
                    time_answer = point[nx]
                    cnt_answer += 1
            else:
                if time_answer > point[nx]:
                    queue.append(nx)

print(time_answer)
print(cnt_answer)