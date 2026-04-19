import sys,heapq

input = sys.stdin.readline

def main():
    visited = [False] * n
    new_cost = get_new_cost(n)
    start_idx = get_start_idx(new_cost,n)
    answer = new_cost[start_idx]
    visited[start_idx] = True
    adj_matrix = get_adj_matrix(n)
    q = init_q(adj_matrix,start_idx)
    while q:
        cost, vx = heapq.heappop(q)
        if visited[vx] == True: continue
        visited[vx] = True
        if new_cost[vx] < cost: cost = new_cost[vx]
        answer += cost
        for nx in range(n):
            if visited[nx] == True: continue
            heapq.heappush(q,(adj_matrix[vx][nx],nx))
    print(answer)

def get_new_cost(n):
    new_cost = []
    for _ in range(n):
        new_cost.append(int(input()))
    return new_cost

def get_start_idx(new_cost,n):
    ret_value = 0
    for i in range(1,n):
        if new_cost[ret_value] > new_cost[i]:
            ret_value = i
    return ret_value

def get_adj_matrix(n):
    ret_value = []
    for _ in range(n):
        ret_value.append(list(map(int,input().split())))
    return ret_value

def init_q(adj_matrix,start_idx):
    q = []
    for i in range(n):
        if i == start_idx: continue
        heapq.heappush(q,(adj_matrix[start_idx][i],i))
    return q

if __name__ == "__main__":
    n = int(input())
    main()