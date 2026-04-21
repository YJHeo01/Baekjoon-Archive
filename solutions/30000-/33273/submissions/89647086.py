import sys

input = sys.stdin.readline

def main():
    global value_list
    value_list = []
    cnt = []
    for _ in range(m):
        x,c = map(int,input().split())
        value_list.append(x)
        cnt.append(c)
    global graph
    graph = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i == j: continue
            if value_list[i] % value_list[j] == 0:
                graph[i].append(j)
    answer = -1
    visited = [False] * m
    for i in range(m):
        if visited[i]: continue
        visited[i] = True
        if cnt[i] >= n:
            answer = max(answer,value_list[i]*n)
            continue
        answer = max(answer,dfs(visited,cnt,i,n-cnt[i],value_list[i]*cnt[i]))
    print(answer)
    
def dfs(visited,cnt,vx,depth,value):
    if depth == 0: return value
    ret_value = -1
    for nx in graph[vx]:
        tmp = min(cnt[nx],depth)
        visited[nx] = True
        ret_value = max(ret_value,dfs(visited,cnt,nx,depth-tmp,value+tmp*value_list[nx]))
    return ret_value

if __name__ == "__main__":    
    n,m = map(int,input().split())
    main()