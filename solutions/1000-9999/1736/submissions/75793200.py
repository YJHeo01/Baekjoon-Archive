n,m = map(int,input().split())

room = []

for _ in range(n):
    room.append(list(map(int,input().split())))

row_trash = [0] * n
column_trash = [0] * m

for i in range(n):
    for j in range(m):
        if room[i][j] == 1:
            row_trash[i] += 1
            column_trash[j] += 1

answer = 0

def move_right(room,row_trash,column_trash,x):
    for y in range(m):
        if room[x][y] == 1:
            room[x][y] = 0
            row_trash[x] -= 1
            column_trash[y] -= 1
            if row_trash[x] == 0:
                return y

def move_down(room,row_trash,column_trash,start):
    x,y = start
    max_trash_column = y
    max_trash_cnt = column_trash[y]
    for i in range(y,m):
        if column_trash[i] >= max_trash_cnt:
            max_trash_cnt = column_trash[i]
            max_trash_column = i
    for i in range(x,n):
        if room[i][max_trash_column] == 1:
            column_trash[max_trash_column] -= 1
            row_trash[i] -= 1
            room[i][max_trash_column] = 0

def cleaner(room,row_trash,column_trash,x):
    y = move_right(room,row_trash,column_trash,x)
    move_down(room,row_trash,column_trash,(x,y))

for i in range(n):
    if row_trash[i] == 0:
        continue
    cleaner(room,row_trash,column_trash,i)
    answer += 1

print(answer)
