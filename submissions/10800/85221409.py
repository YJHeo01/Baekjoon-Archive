import sys

input = sys.stdin.readline

def main():
    n = int(input())
    player = []
    ball_list = [[] for _ in range(n+1)]
    color_cnt = [0] * (n+1)
    prefix_sum_list = [[]]
    for _ in range(n):
        color, size = map(int,input().split())
        player.append((color, size))
        color_cnt[color] += 1
        ball_list[color].append(size)
    for i in range(n+1):
        ball_list[i].sort()
    for color in range(1,n+1):
        prefix_sum = [0] * (color_cnt[color]+1)
        for i in range(color_cnt[color]):
            prefix_sum[i+1] = prefix_sum[i] + ball_list[color][i]
        prefix_sum_list.append(prefix_sum)
    for player_color, player_size in player:
        tmp = 0
        for ball_color in range(1,n+1):
            if player_color == ball_color or color_cnt[ball_color] == 0: continue
            target = -1
            left, right = 0,color_cnt[ball_color]-1
            while left <= right:
                mid = (left+right) // 2
                if ball_list[ball_color][mid] >= player_size:
                    right = mid - 1
                else:
                    left = mid + 1
                    target = mid
            target += 1
            tmp += prefix_sum_list[ball_color][target]
        print(tmp)

if __name__ == "__main__":
    main()