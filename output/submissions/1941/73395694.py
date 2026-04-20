array = []

for _ in range(5):
    array.append(list(input()))

check = [[[False]*5 for _ in range(5)]for _ in range(7)]
def backtracking(x,y,friend_list,power,visited):
    if friend_list == 7:
        if power >= 4:
            return 1
        else:
            return 0
    ret_value = 0
    visited[x][y] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or visited[nx][ny] == True:
            continue
        if array[nx][ny] == 'S':
            ret_value += backtracking(nx,ny,friend_list+1, power+1,visited)
        else:
            ret_value += backtracking(nx,ny,friend_list + 1, power,visited)
    visited[x][y] = False
    return ret_value
        
answer = 0
for i in range(5):
    for j in range(5):
        if array[i][j] == 'S':
            visited = [[False]*5 for _ in range(5)]
            answer += backtracking(i,j,1,1,visited)    

print(answer)