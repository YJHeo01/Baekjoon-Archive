t = int(input())

def team(graph,visited,start):
    vx = start
    while True:
        nx = graph[vx]
        if visited[nx] == True:
            return False
        elif nx == start:
            return True
        else:
            visited[nx] = True
            vx = nx


for _ in range(t):
    n = int(input())
    array = [0] + list(map(int,input().split()))
    answer = 0
    for i in range(1,n+1):
        visited = [False] * (n+1)
        if team(array,visited,i) == False:
            answer += 1
    print(answer)