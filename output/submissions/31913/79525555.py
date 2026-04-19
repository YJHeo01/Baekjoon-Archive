import sys
from collections import deque

input = sys.stdin.readline

def main():
    command = []
    for _ in range(m):
        command.append(list(map(int,input().split())))
    for c in range(1,1000001):
        visited = [[False]*(2**(n+1)) for _ in range(c+1)]
        answer = bfs(command,visited,c)
        if answer != INF:
            break
    if answer == INF: answer = 'INF'
    print(answer)

def bfs(graph,visited,start):
    queue = deque([[start]+[0]])
    visited[start][0] = True
    while queue:
        money, things = queue.popleft()
        for i in range(m):
            next_money = money
            next_things = things
            if graph[i][0] == 1:
                if things & 2 ** graph[i][2] != 0:continue
                next_money -= graph[i][1]
                next_things += 2 ** graph[i][2]
            elif graph[i][0] == 2:
                if things & 2 ** graph[i][1] == 0:continue
                next_money += graph[i][2]
                next_things -= 2 ** graph[i][1]
            elif graph[i][0] == 3:
                if things & 2 ** graph[i][1] == 0 or things & 2 ** graph[i][2] != 0:
                    continue
                next_things -= 2 ** graph[i][1]
                next_things += 2 ** graph[i][2]
            elif graph[i][0] == 4:
                if money < graph[i][2] or things & 2 ** graph[i][1] == 0 or things & 2 ** graph[i][3] != 0:
                    continue
                next_money -= graph[i][2]
                next_things -= 2 ** graph[i][1]
                next_things += 2 ** graph[i][3]
            else:
                if things & 2 ** graph[i][1] == 0 or things & 2 ** graph[i][2] != 0:continue
                next_money += graph[i][3]
                next_things -= 2 ** graph[i][1]
                next_things += 2 ** graph[i][2]
            if next_money > start: return start
            if next_money < 0 or visited[next_money][next_things] == True:continue
            visited[next_money][next_things] = True
            queue.append((next_money,next_things))
    return INF

if __name__ == "__main__":
    n,m = map(int,input().split())
    INF = int(1e9)
    main()