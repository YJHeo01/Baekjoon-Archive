def main():
    global n,m
    n,m = map(int,input().split())
    room = get_room(n)
    answer = solution(room)
    print(answer)

def get_room(n):
    room = []
    for _ in range(n):
        room.append(list(map(int,input().split())))
    return room

def solution(room):
    row_trash = get_row_trash(room)
    column_trash = get_column_trash(room)
    answer = 0
    for i in range(n):
        if row_trash[i] == 0 : continue
        answer += 1
        cleaner(room,row_trash,column_trash,(i,0))
    return answer
            
def get_row_trash(room):
    row_trash = [0] * n
    for i in range(n):
        row_trash[i] = sum(room[i])
    return row_trash

def get_column_trash(room):
    column_trash = [0] * m
    for i in range(m):
        for j in range(n):
            column_trash[i] += room[j][i]
    return column_trash

def cleaner(room,row_trash,column_trash,start):
    x,y = start
    while True:
        y = cleaner_row(room,row_trash,column_trash,(x,y))
        y = get_column(column_trash,y)
        x = cleaner_column(room,row_trash,column_trash,(x,y))
        if x == n-1 and y == m-1: return

def cleaner_row(room,row_trash,column_trash,start):
    row,y = start
    for column in range(y,m):
        if room[row][column] == 0: continue
        room[row][column] = 0
        row_trash[row] -= 1
        column_trash[column] -= 1
        if row_trash[row] == 0: return column
    return m - 1

def get_column(column_trash,y):
    ret_value = y
    for i in range(y+1,m):
        if column_trash[i] > column_trash[ret_value]:
            ret_value = i
    return ret_value

def cleaner_column(room,row_trash,column_trash,start):
    x,column = start
    for row in range(x,n):
        if room[row][column] == 0 : continue
        room[row][column] = 0 
        row_trash[row] -= 1
        column_trash[column] -= 1
        if column_trash[column] == 0: return row
    return n-1

if __name__ == "__main__":
    main()