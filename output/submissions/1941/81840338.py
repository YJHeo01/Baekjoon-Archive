from collections import deque
from itertools import combinations

def main():
    student = [list(input()) for _ in range(5)]
    data = []
    for x in range(5):
        for y in range(5):
            data.append((x,y))
    test_case_list = list(combinations(data,7))
    answer = 0
    for test_case in test_case_list:
        S_cnt = 0
        for x,y in test_case:
            if student[x][y] == 'S': S_cnt += 1
        if S_cnt <= 3: continue
        visited = [[True]*5 for _ in range(5)]
        for x,y in test_case: visited[x][y] = False
        bfs(visited,test_case[0])
        for x,y in test_case:
            if visited[x][y] == False:
                answer -= 1
                break
        answer += 1
    print(answer)

def bfs(vistied,start):
    queue = deque([start])
    vistied[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or vistied[nx][ny] == True: continue
            vistied[nx][ny] = True
            queue.append((nx,ny))

if __name__ == "__main__":
    INF = int(1e9)
    main()