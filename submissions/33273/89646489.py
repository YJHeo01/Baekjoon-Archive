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
    graph = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if value_list[i] % value_list[j] == 0:
                graph[j].append(i)
    answer = -1
    for i in range(m):
        cnt[i] -= 1
        answer = max(answer,dfs(graph,cnt,i,1,value_list[i]))
        cnt[i] += 1
    print(answer)
    
def dfs(graph,cnt,vx,depth,value):
    if depth == n: return value
    ret_value = -1
    for nx in graph[vx]:
        if cnt[nx] == 0: continue
        cnt[nx] -= 1
        ret_value = max(ret_value,dfs(graph,cnt,nx,depth+1,value+value_list[nx]))
        cnt[nx] += 1
    return ret_value

if __name__ == "__main__":    
    n,m = map(int,input().split())
    main()