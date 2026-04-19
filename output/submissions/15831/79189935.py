def main():
    n,b,w = map(int,input().split())
    answer = 0
    array = list(input())
    left,right = 0,0
    blue_cnt, white_cnt = 0,0
    if array[0] == 'B': blue_cnt += 1
    else: white_cnt += 1
    while True:
        if blue_cnt > b:
            if array[left] == 'B': blue_cnt -= 1
            else: white_cnt -= 1
            left += 1
        else:
            if white_cnt >= w:
                answer = max(answer,right-left+1)
            right += 1
            if right >= n: break
            elif array[right] == 'B': blue_cnt += 1
            else: white_cnt += 1
    print(answer)

if __name__ == "__main__":
    main()