n,m = map(int,input().split())

def cleaning(graph,start,direction):
    robot = start
    d = [(-1,0),(0,-1),(1,0),(0,1)]
    ret_value = 1
    graph[start[0]][start[1]] = 2
    while 1:
        non_clean = 1
        for _ in range(4):
            direction = (direction + 1)%4
            nx, ny = robot[0]+d[direction][0], robot[1] + d[direction][1]
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                robot = (nx,ny)
                ret_value += 1
                non_clean = 0
                break
        if non_clean == 1:
            nx, ny = robot[0]-d[direction][0], robot[1] - d[direction][1]
            if graph[nx][ny] == 1:
                return ret_value
            else:
                robot = (nx,ny) 



r,c,d = map(int,input().split())



room = []
for i in range(n):
    tmp = list(map(int,input().split()))
    room.append(tmp)

answer = cleaning(room,(r,c),d)

print(answer)