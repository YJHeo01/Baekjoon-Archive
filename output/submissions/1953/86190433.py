from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    team = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        tmp = list(map(int,input().split()))
        graph[i] += tmp[1:]
    for i in range(1,n+1):
        if team[i] == -1: 
            if i == 1: team[i] = 0
            else: team[i] = 1
            bfs(graph,team,i)
    blue_team, white_team = [], []
    for i in range(1,n+1):
        if team[i] == 0: blue_team.append(i)
        else: white_team.append(i)
    print(len(blue_team))
    print(*blue_team)
    print(len(white_team))
    print(*white_team)

def bfs(graph,team,start):
    queue = deque([start])
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if team[nx] == -1:
                team[nx] = (team[vx]+1) % 2
                queue.append(nx)

if __name__ == "__main__":
    main()