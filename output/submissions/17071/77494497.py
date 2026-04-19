from collections import deque

INF = int(1e9)

def main():
    n,k = map(int,input().split())
    visited = [[INF]*(500001) for _ in range(2)]
    move_Subin(visited,n)
    answer = solution(visited,k)
    print(answer)

def move_Subin(visited,start):
    queue = deque([(start,0)])
    visited[0][start] = 0
    dx = [1,-1]
    while queue:
        vx,vt = queue.popleft()
        nt = (vt+1) % 2
        nx = vx * 2
        if nx <= 500000 and visited[nt][nx] > visited[vt][vx] + 1:
            visited[nt][nx] = visited[vt][vx] + 1
            queue.append((nx,nt))
        for i in range(2):
            nx = vx + dx[i]
            if nx < 0 or nx > 500000:
                continue
            if visited[nt][nx] > visited[vt][vx] + 1:
                visited[nt][nx] = visited[vt][vx] + 1
                queue.append((nx,nt))

def solution(visited,k):
    answer = -1
    time = 0
    while True:
        k += time
        if k > 500000:
            break
        if visited[time%2][k] <= time:
            answer = time
            break
        time += 1
    return answer

if __name__ == "__main__":
    main()