import heapq

def main():
    adj_matrix_A = [list(input()) for _ in range(n)]
    adj_matrix_B = [list(input()) for _ in range(n)]
    distance = [[INF]*(weight_limit+1) for _ in range(n)]
    answer = dijkstra(adj_matrix_A,adj_matrix_B,distance)
    print(answer)

def dijkstra(adj_matrix_A,adj_matrix_B,distance):
    distance[0][0] = 0
    q = []
    heapq.heappush(q,(0,0,0))
    ret_value = INF
    while q:
        weight_a, weight_b, vx = heapq.heappop(q)
        if vx == 1:
            ret_value = min(ret_value,weight_a * weight_b)
            continue
        if weight_b > distance[vx][weight_a] or weight_a * weight_b > INF: continue
        for nx in range(n):
            if adj_matrix_A[vx][nx] == '.': continue
            new_weight_a = weight_a + int(adj_matrix_A[vx][nx])
            new_weight_b = weight_b + int(adj_matrix_B[vx][nx])
            if new_weight_a > weight_limit: continue
            if distance[nx][new_weight_a] > new_weight_b:
                distance[nx][new_weight_a] = new_weight_b
                heapq.heappush(q,(new_weight_a,new_weight_b,nx))
    if ret_value >= INF: ret_value = -1
    return ret_value

if __name__ == "__main__":
    n = int(input())
    weight_limit = 9 * (n-1)
    INF = weight_limit ** 3
    main()