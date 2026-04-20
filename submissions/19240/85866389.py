from collections import deque
import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n,m = map(int,input().split())
        team = [0] * (n+1) #팀 없음 = 0, A팀 = 1, B팀 = 2
        team_A_restrict = [False] * (n+1)
        team_B_restrict = [False] * (n+1)
        graph = [[] for _ in range(n+1)]
        parent = list(range(n+1))
        for _ in range(m):
            a,b = map(int,input().split())
            union_parent(parent,a,b)
            graph[a].append(b)
            graph[b].append(a)
        start = []
        for i in range(1,n+1):
            if parent[i] == i: start.append(i)
        print(solution(graph,team,team_A_restrict,team_B_restrict,start))

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def solution(graph,team,team_A_restrict,team_B_restrict,start):
    queue = deque(start)
    for vx in start:
        if team_A_restrict[vx] == False:
            team[vx] = 1
            for nx in graph[vx]:
                team_A_restrict[nx] = True
                queue.append(nx)
        elif team_B_restrict[vx] == False:
            team[vx] = 2
            for nx in graph[vx]:
                team_B_restrict[nx] = True
                queue.append(nx)
        else:
            return "NO"
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if team[vx] == team[nx]: return "NO"
            if team[vx] == 1:
                if team_B_restrict[nx]: return "NO"
                team_A_restrict[nx] = True
                if team[nx] == 0:
                    team[nx] = 2
                    queue.append(nx)
            else:
                if team_A_restrict[nx]: return "NO"
                team_B_restrict[nx] = True
                if team[nx] == 0:
                    team[nx] = 1
                    queue.append(nx)
    return "YES"

if __name__ == "__main__":
    main()