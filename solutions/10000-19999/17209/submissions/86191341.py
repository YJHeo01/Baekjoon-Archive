from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    adj_matrix = [list(input().rstrip()) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or visited[j][i]: continue
            if adj_matrix[i][j] == '1':
                graph[i].append(j); graph[j].append(i) #소문의 방향이 양방향이던, 단방향이던, 둘 중 한명은 새내기이고, 나머지는 헌내기다.
                visited[i][j] = True; visited[j][i] = True #그래프에 중복 간선을 없애기 위한 절차
    answer = 0    
    team = [-1] * n #헌내기 팀, 새내기 팀이라고 생각했다.
    for i in range(n):
        if team[i] == -1: answer += bfs(graph,team,i) 
    print(answer)

def bfs(graph,team,start): #이분 그래프
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