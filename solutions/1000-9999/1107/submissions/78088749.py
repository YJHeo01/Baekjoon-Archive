from collections import deque

SIZE = 1000001

def main():
    global n
    n = int(input())
    m = int(input())
    if m == 0:
        answer = not_need_fix(n)
        print(answer)
        return
    button = get_button()
    click_cnt = [SIZE] * SIZE
    answer = control(button,click_cnt)
    print(answer)

def not_need_fix(n):
    ret_value = abs(n-100)
    tmp = 1
    while True:
        n = n // 10
        if n == 0:
            break
        tmp += 1
    ret_value = min(ret_value,tmp)
    return ret_value

def get_button():
    button = [True] * 10
    tmp = list(map(int,input().split()))
    for i in tmp:
        button[i] = False
    button_list = []
    for i in range(10):
        if button[i] == False: continue
        button_list.append(i)
    return button_list

def control(button,click_cnt):
    channel_list = click_num_button(button,click_cnt)
    click_plus_minus_button(click_cnt,channel_list)        
    return click_cnt[n]

def click_num_button(button,click_cnt):
    queue = init_queue(button,click_cnt)
    ret_value = [100]
    while queue:
        vx = queue.popleft()
        ret_value.append(vx)
        tmp = vx * 10
        if tmp >= SIZE: continue
        for dx in button:
            nx = tmp + dx
            if nx >= SIZE: break
            if click_cnt[nx] > click_cnt[vx] + 1:
                click_cnt[nx] = click_cnt[vx] + 1
                queue.append(nx)
    return ret_value

def init_queue(button,click_cnt):
    ret_value = deque([])
    for i in button:
        click_cnt[i] = 1
        ret_value.append(i)
    return ret_value

def click_plus_minus_button(click_cnt,start):
    queue = deque(start)
    click_cnt[100] = 0
    while queue:
        vx = queue.popleft()
        nx = get_nx(vx)
        if click_cnt[nx] <= click_cnt[vx] + 1:continue
        click_cnt[nx] = click_cnt[vx] + 1
        queue.append(nx)

def get_nx(vx):
    if vx > n:
        return vx - 1
    return vx + 1

if __name__ == "__main__": 
    main()