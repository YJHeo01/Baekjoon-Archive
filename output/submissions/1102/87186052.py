import heapq

def main():
    adj_matrix = [list(map(int,input().split())) for _ in range(n)]
    distance = [INF] * (2**n)
    first_state = list(input())
    dijkstra(adj_matrix,distance,first_state)
    p = int(input())
    answer = INF
    for state in range(2**n):
        cnt = 0
        tmp = 1
        for _ in range(n):
            if tmp & state != 0: cnt += 1
            tmp <<= 1
        if cnt < p: continue
        answer = min(answer,distance[state])
    if answer >= INF:
        answer = -1
    print(answer)

def dijkstra(adj_matrix,distance,first_state):
    q = []
    tmp = 1
    start = 0
    for i in range(n):
        if first_state[i] == 'Y':
            start |= tmp
        tmp <<= 1
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        vd, state = heapq.heappop(q)
        if vd > distance[state]: continue
        vx_bit = 1
        for vx in range(n):
            if vx_bit & state != 0:
                nx_bit = 1
                for nx in range(n):
                    if nx_bit & state: 
                        nx_bit <<= 1
                        continue
                    nd = vd + adj_matrix[vx][nx]
                    next_state = state | nx_bit
                    if distance[next_state] > nd:
                        distance[next_state] = nd
                        heapq.heappush(q,(nd,next_state))
                    nx_bit <<= 1
            vx_bit <<= 1

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    main()