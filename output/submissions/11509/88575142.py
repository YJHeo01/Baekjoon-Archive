INF = 1000000

n = int(input())

array = list(map(int,input().split()))

balloon = [[] for _ in range(INF+1)]

for i in range(n): balloon[array[i]].append(i)

answer = 0

visited = [False] * n

for i in range(n):
    if visited[i]: continue
    next_high = array[i] - 1
    visited[i] = True
    vx = i
    while True:
        finish = True
        for nx in balloon[next_high]:
            if visited[nx] == False and nx > vx:
                visited[nx] = True
                finish = False
                vx = nx
                break
        next_high -= 1
        if finish or next_high <= 0: break    
    answer += 1

print(answer)