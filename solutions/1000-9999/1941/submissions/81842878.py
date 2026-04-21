from collections import deque
from itertools import combinations

def main():
    student = [list(input()) for _ in range(5)]
    data = get_data()
    test_case_list = list(combinations(data,7))
    answer = 0
    for test_case in test_case_list:
        answer += solution(student,test_case)
    print(answer)

def get_data():
    data = []
    for x in range(5):
        for y in range(5):
            data.append((x,y))
    return data

def solution(student,test_case):
    if get_S_cnt(student, test_case) <= 3: return 0
    
    area = [[False]*5 for _ in range(5)]
    
    for x,y in test_case: area[x][y] = True
    
    bfs(area,test_case[0])
    
    for x,y in test_case:
        if area[x][y] == True: return 0
    
    return 1

def get_S_cnt(student,test_case):
    ret_value = 0
    for x,y in test_case:
        if student[x][y] == 'S': ret_value += 1
    return ret_value

def bfs(area,start):
    queue = deque([start])
    area[start[0]][start[1]] = False
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or area[nx][ny] == False: continue
            area[nx][ny] = False
            queue.append((nx,ny))

if __name__ == "__main__":
    main()