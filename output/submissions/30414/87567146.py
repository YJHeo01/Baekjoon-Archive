import sys

sys.setrecursionlimit(int(1e6)+5)

input = sys.stdin.readline

def main():
    n,p = map(int,input().split())
    visited = [False] * (n+1)
    cur = [0] + list(map(int,input().split()))
    target = [0] + list(map(int,input().split()))
    value = []
    
    for i in range(n+1):
        value.append(cur[i]-target[i])
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited[p] = True
    answer = dfs(graph,visited,value,p,[])
    print(answer)

    
def dfs(graph,visited,soil,vx,stack):
    ret_value = 0
    while stack:
        if soil[vx] >= 0: break
        x, value = stack.pop()
        soil[vx] += value
        if soil[vx] >= 0:
            stack.append((x,soil[vx]))
            soil[vx] = 0
            break

    if soil[vx] > 0:
        stack.append((vx,soil[vx]))
    else:
        ret_value -= soil[vx]

    for nx in graph[vx]:
        if visited[nx]: continue
        visited[nx] = True
        ret_value += dfs(graph,visited,soil,nx,stack)
    
    if stack != []:
        x,value = stack.pop()
        if x != vx:
            stack.append((x,value))

    return ret_value

if __name__ == "__main__":
    main()