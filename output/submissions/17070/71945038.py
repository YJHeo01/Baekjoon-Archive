from collections import deque

n = int(input())

house = []

for i in range(n):
    house.append(list(map(int,input().split())))

visited = [[[0]*n for _ in range(n)] for _ in range(3)]

queue_inserted = [[[False]*n for _ in range(n)]for _ in range(3)]
def check_move_possible(graph,point,d):
    if graph[point[0]][point[1]] != 0:
        return False
    if d == 1:
        if graph[point[0]-1][point[1]] != 0 or graph[point[0]][point[1]-1] != 0:
            return False
    return True

def solution(graph,visited,queue_inserted):
    queue = deque([(0,1,0)])
    visited[0][0][1] = 1
    queue_inserted[0][0][1] = True
    while queue:
        vx, vy, d = queue.popleft()
        if d == 0:#가로
            dx = [0,1]
            for i in range(2):
                nx = vx + dx[i]
                ny = vy + 1
                next_d = d + i
                if nx >= n or ny >= n:
                    continue
                if check_move_possible(graph,(nx,ny),next_d) == False:
                    continue
                visited[next_d][nx][ny] += visited[d][vx][vy]     
                if queue_inserted[next_d][nx][ny] == False:                    
                    queue_inserted[next_d][nx][ny] = True
                    queue.append((nx,ny,next_d))
        elif d == 2:
            dy = [0,-1]
            for i in range(2):
                nx = vx + 1
                ny = vy - dy[i]
                next_d = d - i
                if nx >= n or ny >= n:
                    continue
                if check_move_possible(graph,(nx,ny),next_d) == False:
                    continue
                visited[next_d][nx][ny] += visited[d][vx][vy]
                if queue_inserted[next_d][nx][ny] == False:
                    queue_inserted[next_d][nx][ny] = True
                    queue.append((nx,ny,next_d))
        else:
            dx = [0,1,1]
            dy = [1,1,0]
            for i in range(3):
                nx = vx + dx[i]
                ny = vy + dy[i]
                next_d = i
                if nx >= n or ny >= n:
                    continue
                if check_move_possible(graph,(nx,ny),next_d) == False:
                    continue
                visited[next_d][nx][ny] += visited[d][vx][vy]
                if queue_inserted[next_d][nx][ny] == False:
                    queue_inserted[next_d][nx][ny] = True
                    queue.append((nx,ny,next_d))
    answer = 0
    for i in range(3):
        answer += visited[i][n-1][n-1]
    return answer

print(solution(house,visited,queue_inserted))