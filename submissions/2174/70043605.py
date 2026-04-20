a, b = map(int,input().split())
ground = [[-1]*(a+1) for _ in range(b+1)]
robot = [[]]
direction_list = ['N','E','S','W']
n,m = map(int,input().split())
def spin_clockwise(robot_number,cnt):
   global ground,robot
   x,y = robot[robot_number][0], robot[robot_number][1]
   ground[x][y] = (ground[x][y]+cnt)%4
   return

def spin_counterclockwise(robot_number,cnt):
    global ground,robot
    x,y = robot[robot_number][0], robot[robot_number][1]
    ground[x][y] = (ground[x][y]-cnt)%4
    return

def move_robot(robot_number):
    global ground,robot
    x,y = robot[robot_number][0], robot[robot_number][1]
    direction = ground[x][y]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    nx, ny = x + dx[direction], y + dy[direction]
    if nx <= 0 or ny <= 0 or nx > b or ny > a:
        return robot_number
    elif ground[nx][ny] != -1:
        for i in range(1,n+1):
            if [nx,ny] == robot[i]:
                return [robot_number,i]
    else:
        robot[robot_number] = [nx,ny]
        ground[nx][ny] = ground[x][y]
        ground[x][y] = -1
        return 0


def robot_simulation(robot_number,command,cnt):
    ret_value = 0
    if command == 'L':
        spin_counterclockwise(robot_number,cnt)
    elif command == 'R':
        spin_clockwise(robot_number,cnt)
    else:
        for _ in range(cnt):
            ret_value = move_robot(robot_number)
            if ret_value != 0:
                break
    return ret_value

    
for _ in range(n):
    x,y,direction = input().split()
    x,y = int(x),int(y)
    for i in range(4):
        if direction == direction_list[i]:
            direction = i
            break
    ground[y][x] = direction
    robot.append([y,x])

collision_event = 0
for _ in range(m):
    robot_number, command, cnt = input().split()
    collision_event = robot_simulation(int(robot_number),command,int(cnt))
    if collision_event != 0:
        break

if collision_event == 0:
    print("OK")
else:
    if type(collision_event) == int:
        print("Robot {} crashes into the wall".format(collision_event))
    else:
        print("Robot {} crashes into robot {}".format(str(collision_event[0]),str(collision_event[1])))