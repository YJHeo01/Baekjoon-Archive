from collections import deque

def main():
    yak = list(input())
    visited = [[False]*(3*n+1) for _ in range(3*n+1)]
    bfs(yak,visited)
    answer = 0
    for i in range(3*n+1):
        for j in range(3*n+1):
            if visited[i][j]:
                answer = max(answer,i+j)
    print(answer)

def bfs(yak,visited):
    queue = deque([(0,0)])
    visited[0][0] = True
    eat_type = ['B','L','D']
    while queue:
        popleft_cnt, pop_cnt = queue.popleft()
        if popleft_cnt + pop_cnt >= 3 * n: continue
        today_eat_type = eat_type[(popleft_cnt+pop_cnt)%3]
        if yak[popleft_cnt] == today_eat_type and visited[popleft_cnt+1][pop_cnt] == False:
            visited[popleft_cnt+1][pop_cnt] = True
            queue.append((popleft_cnt+1,pop_cnt))
        if yak[3*n-1-pop_cnt] == today_eat_type and visited[popleft_cnt][pop_cnt+1] == False:
            visited[popleft_cnt][pop_cnt+1] = True
            queue.append((popleft_cnt,pop_cnt+1))

if __name__ == "__main__":
    n = int(input())
    main()
