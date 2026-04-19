from collections import deque

def main():
    n = int(input())
    print(solution(n))

def solution(n):
    queue = deque([1])
    visited = {}
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for dx in [2,3]:
            nx = vx * dx
            if nx == n: return visited[vx] + 1
            if nx > n or nx in visited: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
        nx = vx + 1
        if nx == n: return visited[vx] + 1
        if nx in visited: continue
        visited[nx] = visited[vx] + 1
        queue.append(nx)

if __name__ == "__main__":
    main()