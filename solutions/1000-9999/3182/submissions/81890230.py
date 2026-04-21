def main():
    n = int(input())
    array = [0] + [int(input()) for _ in range(n)]
    max_cnt = 0
    answer = -1
    for i in range(1,n+1):
        visited = [False] * (n+1)
        tmp = dfs(array,visited,i)
        if tmp > max_cnt:
            max_cnt = tmp
            answer = i
    print(answer)

def dfs(array,visited,vx):
    visited[vx] = True
    nx = array[vx]
    if visited[nx] == True:
        return 1
    return dfs(array,visited,nx) + 1

if __name__ == "__main__":
    main()