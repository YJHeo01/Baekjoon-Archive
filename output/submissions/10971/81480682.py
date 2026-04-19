import sys

input = sys.stdin.readline

def main():
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int,input().split())))
    answer = INF
    visited = [False] * n
    for i in range(n):
        visited[i] = True
        answer = min(answer,backtracking(adj_matrix,visited,i,i,0))
        visited[i] = False
    print(answer)

def backtracking(adj_matrix,visited,vx,start,cost):
    ret_value = INF
    finish = True
    for nx in range(n):
        if visited[nx] == False: finish = False
        if adj_matrix[vx][nx] == 0 or visited[nx] == True: continue
        visited[nx] = True
        ret_value = min(ret_value,backtracking(adj_matrix,visited,nx,start,cost+adj_matrix[vx][nx]))
        visited[nx] = False
    if finish == True: ret_value = cost + adj_matrix[vx][start]
    return ret_value

if __name__ == "__main__":
    n = int(input())
    INF = int(1e9)
    main()