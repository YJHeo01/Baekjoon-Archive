import sys,heapq

input = sys.stdin.readline

def main():
    n = int(input())
    planet = []
    visited = [False] * n
    for _ in range(n):
        planet.append(list(map(int,input().split())))
    answer = 0
    visited[0] = True
    q = init_q(planet,n)
    while q:
        dist, vx = heapq.heappop(q)
        if visited[vx] == True:continue
        answer += dist; visited[vx] = True
        for nx in range(n):
            if visited[nx] == True:continue
            heapq.heappush(q,(min(abs(planet[vx][0]-planet[nx][0]),abs(planet[vx][1]-planet[nx][1]),abs(planet[vx][2]-planet[nx][2])),nx))
    print(answer)

def init_q(planet,n):
    q = []
    for i in range(1,n):
        dist = min(abs(planet[0][0]-planet[i][0]),abs(planet[0][1]-planet[i][1]),abs(planet[0][2]-planet[i][2]))
        heapq.heappush(q,(dist,i))
    return q

if __name__ == "__main__":
    main()