from collections import deque

robots = deque([])

n,k = map(int,input().split())
array = list(map(int,input().split()))
robot = [False] * (2*n)
up_position = 0
down_position = n - 1

answer = 1

while True:
    
    # step 1
    up_position = (up_position - 1) % (2*n)
    down_position = (down_position-1) % (2*n)

    # step 2
    start = down_position - 1
    end = up_position
    if end > start:
        end -= (2*n)
    if robot[down_position] == True:
        robot[down_position] = False

    # step 2-1
    for i in range(start,end,-1):
        if robot[i] == False:
            continue
        if robot[i+1] == False and array[i+1] > 0:
            robot[i] = False
            robot[i+1] = True
            array[i+1] -= 1
    if robot[down_position] == True:
        robot[down_position] = False

    # step 3
    if array[up_position] > 0:
        array[up_position] -= 1
        robot[up_position] = True

    # step 4
    tmp = 0
    for i in range(2*n):
        if array[i] == 0:
            tmp += 1
    if tmp >= k:
        break
    else:
        answer += 1

print(answer)