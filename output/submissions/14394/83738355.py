def main():
    cur_board = list(input())
    target_board = list(input())
    color_list = ['R','G','B','Y','*']
    cur_color = {'R':0,'G':0,'B':0,'Y':0,'*':0}
    target_color = {'R':0,'G':0,'B':0,'Y':0,'*':0}
    for i in range(10):
        cur_color[cur_board[i]] += 1
        target_color[target_board[i]] += 1
    answer = 0
    for color in color_list:
        answer += max(0,cur_color[color]-target_color[color])
    print(answer)

if __name__ == "__main__":
    main()