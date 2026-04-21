n,m = map(int,input().split())

ccty_list = []
area = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(m):
        if tmp[j] not in [0,6]:
            ccty_list.append((i,j))
    area.append(tmp)
def detect_area(x,y,dx,dy):
    while 1:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= n or y >= m or area[x][y] == 6:
            return
        if area[x][y] != 0:
            continue
        area[x][y] = '#'
    return
        
def searching_area(num_list):
    for i in range(len(ccty_list)):
        if area[ccty_list[i][0]][ccty_list[i][1]] == 1:
            if num_list[i] == 0:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
            elif num_list[i] == 1:
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
            elif num_list[i] == 2:
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
            else:
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
        elif area[ccty_list[i][0]][ccty_list[i][1]] == 2:
            if num_list[i] % 2 == 0:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
            else:
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
        elif area[ccty_list[i][0]][ccty_list[i][1]] == 3:
            if num_list[i] == 0:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
            elif num_list[i] == 1:
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
            elif num_list[i] == 2:
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
            else:
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
        elif area[ccty_list[i][0]][ccty_list[i][1]] == 4:
            if num_list[i] == 0:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
            elif num_list[i] == 1:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
            elif num_list[i] == 2:
                detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
            else:
                detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
                detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
        else:
            detect_area(ccty_list[i][0],ccty_list[i][1],1,0)
            detect_area(ccty_list[i][0],ccty_list[i][1],0,1)
            detect_area(ccty_list[i][0],ccty_list[i][1],-1,0)
            detect_area(ccty_list[i][0],ccty_list[i][1],0,-1)
    ret_value = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                ret_value += 1
            elif area[i][j] == '#':
                area[i][j] = 0
            else:
                continue
    return ret_value
def backtracking(num_list):
    ret_value = 100
    if len(num_list) == len(ccty_list):
        ret_value = searching_area(num_list)
        return ret_value
    ret_value = min(backtracking(num_list+[0]),backtracking(num_list+[1]),backtracking(num_list+[2]),backtracking(num_list+[3]))
    return ret_value

answer = backtracking([])

print(answer)