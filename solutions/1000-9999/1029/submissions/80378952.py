def main():
    array = []
    for _ in range(n):
        array.append(list(input()))
    adj_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adj_matrix[i][j] = int(array[i][j])
    visited = [False] * n
    visited[0] = True
    print(backtracking(adj_matrix,visited,0,0,1))

def backtracking(adj_matrix,visited,last_artist,last_price,cnt):
    ret_value = cnt
    for nx in range(n):
        if visited[nx] or last_price > adj_matrix[last_artist][nx]: continue
        visited[nx] = True
        ret_value = max(ret_value,backtracking(adj_matrix,visited,nx,adj_matrix[last_artist][nx],cnt+1))
        visited[nx] = False
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()