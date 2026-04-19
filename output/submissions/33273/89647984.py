import sys, heapq

input = sys.stdin.readline

def main():
    global graph
    graph = [[] for _ in range(m)]
    global value_list
    value_list = []
    cnt = []
    q = []
    for i in range(m):
        x,c = map(int,input().split())
        heapq.heappush(q,(-x,i))
        value_list.append(x)
        cnt.append(c)
    start = [True] * m
    for i in range(m):
        for j in range(m):
            if i == j: continue
            if value_list[i] % value_list[j] == 0:
                graph[i].append((j,value_list[j]))
                start[j] = False
    for i in range(m):
        graph[i].sort(key=lambda x:-x[1])
    answer = -1
    visited = [False] * m
    while q:
        tmp, i = heapq.heappop(q)
        if start[i] == False: continue
        visited[i] = True
        if cnt[i] >= n:
            answer = max(answer,value_list[i]*n)
            break
        answer = max(answer,dfs(visited,cnt,i,n-cnt[i],value_list[i]*cnt[i]))
    print(answer)
    
def dfs(visited,cnt,vx,depth,value):
    ret_value = -1
    if depth == 0: return value
    for nx,dd in graph[vx]:
        if visited[nx]: continue
        tmp = min(cnt[nx],depth)
        visited[nx] = True
        val = dfs(visited,cnt,nx,depth-tmp,value+tmp*dd)
        ret_value = max(ret_value,val)
        if val == -1: visited[nx] = False
    return ret_value

if __name__ == "__main__":    
    n,m = map(int,input().split())
    main()