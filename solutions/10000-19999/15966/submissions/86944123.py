import sys

sys.setrecursionlimit(10**6+5)

def main():
    n = int(input())
    array = list(map(int,input().split()))
    visited = [0] * n
    idx_of_value = [[] for _ in range(INF+1)]
    value_cnt = [0] * (INF+1)
    for i in range(n):
        value = array[i]
        idx_of_value[value].append(i)
        value_cnt[value] += 1
    for i in range(n):
        if visited[i] != 0: continue
        visited[i] = 1
        dfs(array,idx_of_value,value_cnt,visited,i)
    answer = max(visited)
    print(answer)

def dfs(array,idx_of_value,value_cnt,visited,vx):
    if array[vx] == INF: return
    next_value = array[vx] + 1
    next_value_cnt = value_cnt[next_value]
    nx = -1
    left, right = 0, next_value_cnt-1
    while left <= right:
        mid = (left+right) // 2
        if idx_of_value[next_value][mid] > vx:
            nx = idx_of_value[next_value][mid]
            right = mid - 1
        else:
            left = mid + 1
    if nx > vx and visited[nx] <= visited[vx]:
        visited[nx] = visited[vx] + 1
        dfs(array,idx_of_value,value_cnt,visited,nx)

if __name__ == "__main__":
    INF = 1000000
    main()