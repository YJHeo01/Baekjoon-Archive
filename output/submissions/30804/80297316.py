def main():
    n = int(input())
    fruit_list = list(map(int,input().split()))
    left, right = 0,0
    fruit_cnt = [0] * 10
    type_cnt = 0
    answer = 0
    while True:
        if right >= n:break
        if fruit_cnt[fruit_list[right]] == 0:
            type_cnt += 1
        fruit_cnt[fruit_list[right]] += 1
        if type_cnt >= 3:
            while True:
                if type_cnt <= 2:
                    break
                fruit_cnt[fruit_list[left]] -= 1
                if fruit_cnt[fruit_list[left]] == 0:
                    type_cnt -= 1
                left += 1
        right += 1
        answer = max(answer,right-left)
    print(answer)

if __name__ == "__main__":
    main()