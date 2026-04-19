from collections import deque
import sys

input = sys.stdin.readline


def main():
    INF = int(1e9)
    adj_matrix = [[False]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        adj_matrix[a][b] = True
        adj_matrix[b][a] = True
    q = int(input())
    for _ in range(q):
        a,i,j = map(int,input().split())
        if a == 1:
            adj_matrix[i][j],adj_matrix[j][i] = True,True
        else:
            adj_matrix[j][i],adj_matrix[i][j] = False,False
        visited = [-1] * (n+1)
        bfs(adj_matrix,visited)
        print(*visited[1:])
        
def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in range(n+1):
            if visited[nx] != -1 or graph[vx][nx] == False: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
    
if __name__ == "__main__":
    n,m = map(int,input().split())
    main()