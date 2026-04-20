def main():
    n = int(input())
    array = [0] + [int(input()) for _ in range(n)]
    answer = 0
    cnt = [-1] * (n+1)
    for i in range(1,n+1):
        if cnt[i] != -1: continue
        visited = [False] * (n+1)
        if dfs(array,visited,cnt,i) > cnt[answer]:
            answer = i   
    print(answer)

def dfs(array,visited,cnt,vx):
    nx = array[vx]
    if visited[nx] == True:
        cnt[vx] = 1
    else:
        visited[vx] = True
        cnt[vx] = dfs(array,visited,cnt,nx) + 1
    return cnt[vx]

if __name__ == "__main__":
    main()