import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    team = [-1] * (n+1)
    answer = 1
    for i in range(1,n+1):
        if team[i] == -1:
            team[i] = 0
            answer = min(answer,solution(graph,team,i))
    print(answer)

def solution(graph,team,vx):
    ret_value = 1
    for nx in graph[vx]:
        if team[vx] == team[nx]: return 0
        if team[nx] == -1:
            team[nx] = (team[vx] + 1) % 2
            ret_value = min(ret_value,solution(graph,team,nx))
    return ret_value
        
if __name__ == "__main__":
    main()