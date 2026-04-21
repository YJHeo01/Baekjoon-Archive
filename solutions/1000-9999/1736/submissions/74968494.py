n,m = map(int,input().split())

room = []

row_trash = [0] * n
column_trash = [0] * m

for i in range(n):
    tmp = list(map(int,input().split()))
    row_trash[i] = sum(tmp)
    room.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            column_trash[j] += 1


last_complete_column = m

for i in range(m-1,-1,-1):
    if column_trash[i] == 0:
        last_complete_column = i
    else:
        break

answer = 0

def move_right(graph,x,column_trash):
    y = 0
    while True:
        if graph[x][y] == 1:
            graph[x][y] = 0
            column_trash[y] -= 1
        y += 1
        if y == m:
            break

def move_down(graph,cleaner,row_trash):
    x,y = cleaner
    while True:
        if graph[x][y] == 1:
            graph[x][y] = 0
            row_trash[x] -= 1
        x += 1
        if x == n:
            break
def get_next_cleaner_column(column_trash,idx):
    while True:
        if column_trash[idx] == 0:
            idx -= 1
        else:
            break
        if idx < 0:
            return -1
    return idx
def move_cleaner(graph,cleaner_x,row_trash,column_trash,next_cleaner_column):
    move_right(graph,cleaner_x,column_trash)
    next_cleaner_column = get_next_cleaner_column(column_trash,next_cleaner_column)
    if next_cleaner_column < 0:
        return
    move_down(graph,(cleaner_x,next_cleaner_column),row_trash)
        


for i in range(n):
    if row_trash[i] == 0:
        continue
    answer += 1
    move_cleaner(room,i,row_trash,column_trash,last_complete_column-1)

print(answer)