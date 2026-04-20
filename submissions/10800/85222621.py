import sys

input = sys.stdin.readline

def main():
    player, all_ball_list = [], []
    color_ball_list = [[] for _ in range(n+1)]
    color_cnt = [0] * (n+1)
    
    init(player,color_cnt,all_ball_list,color_ball_list)
    prefix_sum_of_color = init_prefix_sum_of_color(color_ball_list,color_cnt)
    prefix_sum_of_all_ball = [0] * (n+1)
    all_ball_list.sort()
    
    for i in range(n):
        prefix_sum_of_all_ball[i+1] = prefix_sum_of_all_ball[i] + all_ball_list[i]

    for player_color, player_size in player:
        tmp_a = binary_search(all_ball_list,n,player_size)
        tmp_b = binary_search(color_ball_list[player_color],color_cnt[player_color],player_size)
        print(prefix_sum_of_all_ball[tmp_a]-prefix_sum_of_color[player_color][tmp_b])

def init(player,color_cnt,all_ball_list,color_ball_list):
    for _ in range(n):
        color, size = map(int,input().split())
        player.append((color, size))
        color_cnt[color] += 1
        all_ball_list.append(size)
        color_ball_list[color].append(size)
    for i in range(n+1):
        color_ball_list[i].sort()

def init_prefix_sum_of_color(color_ball_list,color_cnt):
    ret_value = [[]]
    for color in range(1,n+1):
        prefix_sum = [0] * (color_cnt[color]+1)
        for i in range(color_cnt[color]):
            prefix_sum[i+1] = prefix_sum[i] + color_ball_list[color][i]
        ret_value.append(prefix_sum)
    return ret_value

def binary_search(ball_list,length,target_size,):
    ret_value = -1
    left, right = 0,length-1
    while left<=right:
        mid = (left+right) // 2
        if ball_list[mid] >= target_size:
            right = mid - 1
        else:
            left = mid + 1
            ret_value = mid
    return ret_value + 1

if __name__ == "__main__":
    n = int(input())
    main()