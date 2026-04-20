n = int(input())
answer = 0
student = n*n
classroom = [[0]*(n+1) for _ in range(n+1)]
student_information = [[0]*4 for _ in range(student+1)]

def search_side_seat(seat,search_friend_list):
    search_student_cnt = 0
    x, y = seat[0], seat[1]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx > n or ny > n or nx <= 0 or ny <= 0:
            continue
        if classroom[nx][ny] in search_friend_list:
            search_student_cnt += 1
    return search_student_cnt

def search_student_seat(favorite_student_list):
    best_seat = [1,1]
    best_seat_favorite_student_cnt = 0
    for x in range(1,n+1):
        for y in range(1,n+1):
            if classroom[x][y] != 0:
                continue
            seat = [x,y]
            seat_favorite_student_cnt = search_side_seat(seat,favorite_student_list)
            if seat_favorite_student_cnt > best_seat_favorite_student_cnt: #조건 1
                best_seat = seat
                best_seat_favorite_student_cnt = seat_favorite_student_cnt
            elif seat_favorite_student_cnt == best_seat_favorite_student_cnt:#조건 2
                if search_side_seat(seat,[0]) > search_side_seat(best_seat,[0]):#조건 3을 위해 > 사용
                    best_seat = seat
            else:
                continue
    return best_seat

def search_answer(student_seat):
    answer = 0
    x,y = student_seat
    student_num = classroom[x][y]
    favorite_student_list = student_information[student_num]
    happy_point = search_side_seat(student_seat,favorite_student_list)
    if happy_point > 0:
        answer += 10 ** (happy_point-1)
    return answer

for _ in range(student):
    tmp = list(map(int,input().split()))
    student_num,favorite_student = tmp[0],tmp[1:]
    student_information[student_num] = favorite_student
    best_seat = search_student_seat(favorite_student)
    x,y = best_seat
    classroom[x][y] = student_num

for i in range(1,n+1):
    for j in range(1,n+1):
        answer += search_answer((i,j))

print(answer)