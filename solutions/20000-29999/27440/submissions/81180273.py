import heapq

def main():
    n = int(input())
    print(solution(n))

def solution(n):
    q = []
    visited = {}
    visited[n] = 0
    heapq.heappush(q,(0,n))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > visited[vx]: continue
        for dx in [2,3]:
            nx = (vx-vx%dx) // dx
            if nx not in visited or visited[nx] > visited[vx] + 1 + vx % dx:
                visited[nx] = visited[vx] + 1 + vx % dx
                if nx != 1: heapq.heappush(q,(visited[nx],nx))
    return visited[1]
            
if __name__ == "__main__":
    main()