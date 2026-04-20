import sys, heapq

input = sys.stdin.readline

def main():
    global n,s
    n,s = map(int,input().split())
    minus = 0
    jump = []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        if tmp[0] >= s or tmp[1] == 0: minus += 1
        else: jump.append(tmp)
    n -= minus
    jump.sort()
    distance = [INF] * n
    answer = solution(jump,distance)
    if answer >= INF:
        print("Ducks can't fly")
    else:
        print(answer)

def solution(jump,distance):
    q = []
    ret_value = INF
    for i in range(n):
        if jump[i][0] != 0: break
        distance[i] = 0
        heapq.heappush(q,(0,i))
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx] or dist + s - jump[vx][0] >= ret_value: continue
        if jump[vx][0] + jump[vx][1] >= s:
            ret_value = min(ret_value,dist+s-jump[vx][0])
            continue
        for nx in range(vx+1,n):
            if jump[nx][0] > jump[vx][0] + jump[vx][1]: break
            next_dist = dist + jump[vx][1] + jump[vx][0] + jump[vx][1] - jump[nx][0]
            if distance[nx] > next_dist:
                distance[nx] = next_dist
                heapq.heappush(q,(next_dist,nx))
    return ret_value

if __name__ == "__main__":
    INF = int(1e15)
    main()