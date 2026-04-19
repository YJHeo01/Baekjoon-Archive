from collections import deque

SIZE = 1000001

n = int(input())
m = int(input())

button = [True] * 10
if m != 0:
    tmp = list(map(int,input().split()))
    for idx in tmp:
        button[idx] = False

button_list = []
click_button_cnt = [SIZE] * SIZE
start = []
channel_list = [100]
for i in range(10):
    if button[i] == False:
        continue
    button_list.append(i)
    click_button_cnt[i] = 1
    start.append(i)
    channel_list.append(i)


def click_number_button(button_list,click_button_cnt,start):
    queue = deque(start)
    ret_value = []
    while queue:
        channel = queue.popleft()
        tmp_channel = 10 * channel
        for clicked_button in button_list:
            next_channel = tmp_channel + clicked_button
            if next_channel >= SIZE:
                continue
            if click_button_cnt[next_channel] > click_button_cnt[channel] + 1:
                if click_button_cnt[next_channel] == SIZE:
                    ret_value.append(next_channel)
                click_button_cnt[next_channel] = click_button_cnt[channel] + 1
                queue.append(next_channel)
    return ret_value


channel_list += click_number_button(button_list,click_button_cnt,start)
click_button_cnt[100] = 0

def click_plus_minus_button(click_button_cnt,start):
    queue = deque(start)
    while queue:
        channel = queue.popleft()
        if channel - 1 >= 0 and click_button_cnt[channel-1] > click_button_cnt[channel] + 1:
            click_button_cnt[channel-1] = click_button_cnt[channel] + 1
            queue.append(channel-1)
        if channel + 1 <= 500000 and click_button_cnt[channel+1] > click_button_cnt[channel] + 1:
            click_button_cnt[channel+1] = click_button_cnt[channel] + 1
            queue.append(channel+1)

click_plus_minus_button(click_button_cnt,channel_list)
print(click_button_cnt[n])