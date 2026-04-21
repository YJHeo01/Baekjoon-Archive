n = int(input())

ball_list = list(input())

start = 0

def check_move_cnt(color):
    start = 0
    ret_value = 0
    for i in range(n):
        if ball_list[i] == color:
            start = i
            break
    for i in range(start,n,1):
        if ball_list[i] != color:
            ret_value += 1
    return ret_value

def check_move_cnt_reverse(color):
    start = 0
    ret_value = 0
    for i in range(n-1,-1,-1):
        if ball_list[i] == color:
            start = i
            break
    for i in range(start,-1,-1):
        if ball_list[i] != color:
            ret_value += 1
            
    return ret_value

answer = int(1e9)            

answer = min(check_move_cnt('R'),check_move_cnt('B'),check_move_cnt_reverse('R'),check_move_cnt_reverse('B'))

print(answer)