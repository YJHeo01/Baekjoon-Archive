get_answer = False

puzzle = []

for _ in range(9):
    puzzle.append(list(input()))


def check_row(graph,point,value_list):
    y = point[1]
    for x in range(9):
        value_list[int(graph[x][y])] = False

def check_column(graph,point,value_list):
    x = point[0]
    for y in range(9):
        value_list[int(graph[x][y])] = False

def check_box(graph,point,value_list):
    x,y = point
    if x < 3:
        x1,x2 = 0,3
    elif x >= 6:
        x1,x2 = 6,9
    else:
        x1,x2 = 3,6
    if y < 3:
        y1,y2 = 0,3
    elif y >= 6:
        y1,y2 = 6,9
    else:
        y1,y2 = 3,6
    for r in range(x1,x2):
        for c in range(y1,y2):
            value_list[int(graph[r][c])] = False

def solution(graph,point):
    global get_answer
    if get_answer == True:
        return
    vx,vy = point
    if point == (8,8):
        get_answer = True
        for i in range(9):
            for j in range(9):
                print(graph[i][j],end="")
            print()
    value = [True] * 10
    if graph[vx][vy] != '0': 
        if vy == 8:
            solution(graph,(vx+1,0))
        else:
            solution(graph,(vx,vy+1))
    else:
        check_row(graph,point,value)
        check_column(graph,point,value)
        check_box(graph,point,value)
        for i in range(1,10):
            if value[i] == True:
                graph[vx][vy] = str(i)
                if vy == 8:
                    solution(graph,(vx+1,0))
                else:
                    solution(graph,(vx,vy+1))
                graph[vx][vy] = '0'

solution(puzzle,(0,0))  