import sys

input = sys.stdin.readline

n,m = map(int,input().split())

visited = [False] * (n+1)

answer = n

for _ in range(m):
    command = list(map(int,input().split()))
    if command[0] == 1:
        if visited[command[1]] == False:
            visited[command[1]] = True
            answer -= 1
    elif command[0] == 2:
        if visited[command[1]] == True:
            visited[command[1]] = False
            answer += 1
    else:
        print(answer)