import heapq

def main():
    adj_matrix_A = [list(input()) for _ in range(n)]
    adj_matrix_B = [list(input()) for _ in range(n)]
    INF = int(1e9)
    weight = [[INF]*2 for _ in range(n)]
    dijkstra(adj_matrix_A,adj_matrix_B,weight)
    answer = weight[1][0] * weight[1][1]
    if answer >= INF: answer = -1
    print(answer)

def dijkstra(adj_matrix_A,adj_matrix_B,distance):
    distance[0][0], distance[0][1] = 0,0
    q = []
    heapq.heappush(q,(0,0,0))
    while q:
        weight_a, weight_b, vx = heapq.heappop(q)
        if weight_a * weight_b > distance[vx][0] * distance[vx][1]:
            continue
        for nx in range(n):
            if adj_matrix_A[vx][nx] == '.': continue
            new_weight_a = weight_a + int(adj_matrix_A[vx][nx])
            new_weight_b = weight_b + int(adj_matrix_B[vx][nx])
            if distance[nx][0] * distance[nx][1] == new_weight_a * new_weight_b:
                if abs(distance[nx][0]-distance[nx][1]) > abs(new_weight_a-new_weight_b):
                    distance[nx][0] = new_weight_a
                    distance[nx][1] = new_weight_b
                    heapq.heappush(q,(new_weight_a,new_weight_b,nx))
            if distance[nx][0] * distance[nx][1] > new_weight_a * new_weight_b:
                distance[nx][0] = new_weight_a
                distance[nx][1] = new_weight_b
                heapq.heappush(q,(new_weight_a,new_weight_b,nx))

if __name__ == "__main__":
    n = int(input())
    main()