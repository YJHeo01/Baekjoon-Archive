answer = 0

r, c = map(int,input().split())

def backtracking(graph,visited,start,i):
    global answer
    i += 1
    answer = max(answer,i)
    visited.append(graph[start[0]][start[1]])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for j in range(4):
        nx = start[0] + dx[j]
        ny = start[1] + dy[j]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if graph[nx][ny] not in visited:
            backtracking(graph,visited,(nx,ny),i)
    visited.pop()
    return


board = []

for _ in range(r):
    board.append(list(input()))

backtracking(board,[],(0,0),0)

print(answer)
