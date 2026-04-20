import heapq

def main():
    answer = INF
    adj_matrix = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        distance = [[INF]*n for _ in range(1<<n)]
        answer = min(answer,solution(adj_matrix,distance,i))
        break
    print(answer)


def solution(adj_matrix,distance,start):
    q = []
    distance[1<<start][start] = 0
    heapq.heappush(q,(0,1<<start,start))
    ret_value = INF
    while q:
        dist, state, cur_node = heapq.heappop(q)
        if state == all_visit and adj_matrix[cur_node][start] != 0:
            ret_value = min(ret_value,dist+adj_matrix[cur_node][start])
        if dist > distance[state][cur_node] or state == all_visit: continue
        tmp = 1
        for next_node in range(n):
            if adj_matrix[cur_node][next_node] != 0:
                next_dist = dist + adj_matrix[cur_node][next_node]
                next_state = state | tmp
                if distance[next_state][next_node] > next_dist:
                    distance[next_state][next_node] = next_dist
                    heapq.heappush(q,(next_dist,next_state,next_node))
            tmp <<= 1
    return ret_value

if __name__ == "__main__":
    INF = int(1e15)
    n = int(input())
    all_visit = (1 << n) - 1
    main()