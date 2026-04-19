import sys, heapq

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        answer = solution()
        print(answer)

def solution():
    n,m,p,q = map(int,input().split())
    graph = get_graph(n,m)
    visited = [False] * (n+1)
    visited[1] = True
    prior_q = init_prior_q(graph,p,q)
    while prior_q:
        prior, p_or_q, vx = heapq.heappop(prior_q)
        if visited[vx] == True: continue
        if p_or_q == 0: return "YES"
        visited[vx] = True
        for nx, w in graph[vx]:
            if visited[nx] == True: continue
            next_p_or_q = get_next_p_or_q(p,q,vx,nx)
            heapq.heappush(prior_q,(w,next_p_or_q,nx))
    return "NO"      

def get_graph(n,m):
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph

def init_prior_q(graph,p,q):
    prior_q = []
    for nx, w in graph[1]:
        prior = get_next_p_or_q(p,q,1,nx)
        heapq.heappush(prior_q,(w,prior,nx))
    return prior_q

def get_next_p_or_q(p,q,vx,nx):
    prior = 2
    if vx == p or vx == q: prior -= 1
    if nx == p or nx == q: prior -= 1
    return prior

if __name__ == "__main__":
    main()