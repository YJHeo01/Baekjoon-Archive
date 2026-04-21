def main():
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int,input().split())))
    for x in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][x]+adj_matrix[x][j])
    visited = [False] * n
    answer = solution(adj_matrix,visited,k)
    print(answer)

def solution(adj_matrix,visited,vx):
    ret_value = INF
    visited[vx] = True
    for nx in range(n):
        if visited[nx] == True: continue
        ret_value = min(ret_value,solution(adj_matrix,visited,nx)+adj_matrix[vx][nx])
    visited[vx] = False
    if ret_value == INF: return 0
    return ret_value

if __name__ == "__main__":
    n,k = map(int,input().split())
    INF = int(1e9)
    main()