gear_state = [[]]

gear_left = [6,6,6,6,6]
gear_mid = [0,0,0,0,0]
gear_right = [2,2,2,2,2]


def move_gear(idx,direction): #direction == 1 시계
    global gear_left,gear_mid,gear_right
    gear_left[idx] -= direction
    gear_mid[idx] -= direction
    gear_right[idx] -= direction
    gear_left[idx] %= 8
    gear_right[idx] %= 8
    gear_mid[idx] %= 8


def solution(gear_idx,direction):
    move_gear_list = [(gear_idx,direction)]
    for i in range(1,4):
        if gear_idx - i <= 0:
            break
        if gear_state[gear_idx-i+1][gear_left[gear_idx-i+1]] != gear_state[gear_idx-i][gear_right[gear_idx-i]]:
            if i == 2:
                move_gear_list.append((gear_idx-i,direction))
            else:
                move_gear_list.append((gear_idx-i,-direction))
        else:
            break
    for i in range(1,4):
        if gear_idx + i > 4:
            break
        if gear_state[gear_idx+i][gear_left[gear_idx+i]] != gear_state[gear_idx+i-1][gear_right[gear_idx+i-1]]:
            if i == 2:
                move_gear_list.append((gear_idx+i,direction))
            else:
                move_gear_list.append((gear_idx+i,-direction))
        else:
            break
    for gear in move_gear_list:
        move_gear(gear[0],gear[1])

for _ in range(4):
    gear_state.append(list(input()))

answer = 0

command_cnt = int(input())
for _ in range(command_cnt):
    gear_idx, direction = map(int,input().split())
    solution(gear_idx,direction)
for i in range(1,5):
    if gear_state[i][gear_mid[i]] == '1':
        answer += 2**(i-1)
print(answer)