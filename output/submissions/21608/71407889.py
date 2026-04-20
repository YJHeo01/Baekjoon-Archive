#https://github.com/YJHeo01

import sys
input = sys.stdin.readline
student_procedure = []

n = int(input())
like_student = [[] for _ in range(n**2+1)]
for _ in range(n**2):
    student = list(map(int,input().split()))
    for i in range(1,5):
        like_student[student[0]].append(student[i])
    student_procedure.append(student[0])


classroom = [[0]*n for _ in range(n)]

def search_like_student_cnt(student_num,point):
    ret_value = 0
    x = point[0]
    y = point[1]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if classroom[nx][ny] in like_student[student_num]:
            ret_value += 1
    return ret_value

def search_void_space_cnt(point):
    ret_value = 0
    x = point[0]
    y = point[1]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if classroom[nx][ny] == 0:
            ret_value += 1
    return ret_value

for student in student_procedure:
    best_point = (-1,-1)
    like_student_cnt = 0
    void_space_cnt = 0
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                if best_point == (-1,-1):
                    best_point = (i,j)
                tmp_like = search_like_student_cnt(student,(i,j))
                if tmp_like > like_student_cnt:
                    like_student_cnt = tmp_like
                    void_space_cnt = search_void_space_cnt((i,j))
                    best_point = (i,j)
                elif like_student_cnt == tmp_like:
                    tmp_void = search_void_space_cnt((i,j))
                    if tmp_void > void_space_cnt:
                        void_space_cnt = tmp_void
                        best_point = (i,j)
    classroom[best_point[0]][best_point[1]] = student

answer = 0
for i in range(n):
    for j in range(n):
        student_num = classroom[i][j]
        like_student_cnt = search_like_student_cnt(student_num,(i,j))
        if like_student_cnt != 0:
            answer += 10 ** (like_student_cnt-1)

print(answer)