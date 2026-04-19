n,m = map(int,input().split())

length = min(n,m)

graph = []

for _ in range(n):
    graph.append(list(input()))

answer = -1

while True:
    dx = [length-1,0,length-1]
    dy = [0,length-1,length-1]
    for i in range(n-length+1):
        for j in range(m-length+1):
            x,y = i,j
            correct_answer = True
            for k in range(3):
                nx = x + dx[k]
                ny = y + dy[k]
                if graph[nx][ny] != graph[x][y]:
                    correct_answer = False
                    break
            if correct_answer == True:
                answer = length ** 2
                break
    if answer > 0:
        break
    length -= 1
print(answer)