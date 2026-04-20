gear_state = [[]]
answer = 0
gear_left = [6,6,6,6,6]
gear_mid = [0,0,0,0,0]
gear_right = [2,2,2,2,2]


def movecounterclockwise(idx): 
    global gear_left,gear_mid,gear_right
    gear_left[idx] = ((gear_left[idx] + 1)%8)
    gear_mid[idx] = ((gear_mid[idx] + 1)%8)
    gear_right[idx] = ((gear_right[idx] + 1)%8)

def moveclockwise(idx): 
    global gear_left,gear_mid,gear_right
    gear_left[idx] = ((gear_left[idx] - 1)%8)
    gear_mid[idx] = ((gear_mid[idx] - 1)%8)    
    gear_right[idx] = ((gear_right[idx] - 1)%8)


def left_gear_check(gear_idx,direction):
    move_gear_list = []
    for i in range(1,4):
        if gear_idx - i <= 0:
            break
        if gear_state[gear_idx-i+1][gear_left[gear_idx-i+1]] != gear_state[gear_idx-i][gear_right[gear_idx-i]]:
            move_gear_list.append((gear_idx-i,direction*((-1)**i)))
        else:
            break
    return move_gear_list


def right_gear_check(gear_idx,direction):
    move_gear_list = []
    for i in range(1,4):
        if gear_idx + i > 4:
            break
        if gear_state[gear_idx+i][gear_left[gear_idx+i]] != gear_state[gear_idx+i-1][gear_right[gear_idx+i-1]]:
            move_gear_list.append((gear_idx+i,direction*((-1)**i)))
        else:
            break
    return move_gear_list

def solution(gear_idx,direction):
    move_gear_list = [(gear_idx,direction)]
    move_gear_list += left_gear_check(gear_idx,direction)
    move_gear_list += right_gear_check(gear_idx,direction)

    for gear in move_gear_list:
        if gear[1] == 1:
            moveclockwise(gear[0])
        else:
            movecounterclockwise(gear[0])

for _ in range(4):
    gear_state.append(list(input()))

command_cnt = int(input())
for _ in range(command_cnt):
    gear_idx, direction = map(int,input().split())
    solution(gear_idx,direction)
for i in range(1,5):
    if gear_state[i][gear_mid[i]] == '1':
        answer += 2**(i-1)
print(answer)
        