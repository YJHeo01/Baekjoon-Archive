n = int(input())

yes_or_no = 0

road = []
teachers = []
for i in range(n):
    tmp = list(input().split())
    for j in range(n):
        if tmp[j] == 'T':
            teachers.append((i,j))
    road.append(tmp)

def dfs(block1,block2,block3):
    ret_value = 1
    road[block1[0]][block1[1]] = 'O'
    road[block2[0]][block2[1]] = 'O'
    road[block3[0]][block3[1]] = 'O'
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for teacher in teachers:
        vx, vy = teacher
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            while nx >= 0 and ny >= 0 and nx < n and ny < n:
                if road[nx][ny] == 'O':
                    break
                elif road[nx][ny] == 'S':
                    ret_value = 0
                    road[block1[0]][block1[1]] = 'X'
                    road[block2[0]][block2[1]] = 'X'
                    road[block3[0]][block3[1]] = 'X'
                    return ret_value
                nx = nx + dx[i]
                ny = ny + dy[i]
    road[block1[0]][block1[1]] = 'X'
    road[block2[0]][block2[1]] = 'X'
    road[block3[0]][block3[1]] = 'X'
    return ret_value
l = n**2
for i in range(2,l):
    for j in range(0,l-2):
        for k in range(j+1,i):
            block_1_x,block_1_y = i//n,i%n
            block_2_x,block_2_y = j//n,j%n
            block_3_x,block_3_y = k//n,k%n
            if road[block_1_x][block_1_y] == 'X' and road[block_2_x][block_2_y] == 'X' and road[block_3_x][block_3_y] == 'X':
                yes_or_no += dfs((block_1_x,block_1_y),(block_2_x,block_2_y),(block_3_x,block_3_y))

if yes_or_no > 0:
    print('YES')
else:
    print('NO')