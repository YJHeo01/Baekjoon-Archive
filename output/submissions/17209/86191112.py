from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    adj_matrix = [list(input().rstrip()) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    non_target = [True] * n
    for i in range(n):
        for j in range(n):
            if visited[i][j] or visited[j][i]: continue
            if adj_matrix[i][j] == '1':
                graph[i].append(j); graph[j].append(i)
                visited[i][j] = True; visited[j][i] = True
                non_target[i], non_target[j] = False, False
    answer = 0
    for i in range(n): if non_target[i]: answer += 1
    
    team = [-1] * n
    for i in range(n):
        if non_target[i]: continue
        if team[i] == -1:
            answer += bfs(graph,team,i)
    print(answer)

def bfs(graph,team,start):
    queue = deque([start])
    ret_value = [0] * 2
    team[start] = 0
    while queue:
        vx = queue.popleft()
        ret_value[team[vx]] += 1
        for nx in graph[vx]:
            if team[nx] == -1:
                team[nx] = (team[vx] + 1) % 2
                queue.append(nx)
    return max(ret_value)

if __name__ == "__main__":
    main()