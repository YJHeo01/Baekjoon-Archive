def main():
    weight_first = [list(input()) for _ in range(n)]
    weight_second = [list(input()) for _ in range(n)]
    visited = [False] * n
    visited[0] = True
    answer = backtracking(weight_first,weight_second,visited,0,0,0)
    if answer >= INF: answer = -1
    print(answer)

def backtracking(weight_first,weight_second,visited,vx,A,B):
    if vx == 1: return A * B
    ret_value = INF
    for nx in range(n):
        if weight_first[vx][nx] == '.' or visited[nx]: continue
        visited[nx] = True
        ret_value = min(ret_value,backtracking(weight_first,weight_second,visited,nx,A+int(weight_first[vx][nx]),B+int(weight_second[vx][nx])))
        visited[nx] = False
    return ret_value

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    main()