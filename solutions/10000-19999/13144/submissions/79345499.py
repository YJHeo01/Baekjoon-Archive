def main():
    n = int(input())
    array = list(map(int,input().split()))
    left, right, combo = 0, 0, 0
    num_cnt = [0] * 100001
    answer = 0
    while True:
        if right >= n:break
        num_cnt[array[right]] += 1
        if num_cnt[array[right]] == 1:    
            combo += 1
        else:
            while True:
                num_cnt[array[left]] -= 1; left += 1
                if num_cnt[array[right]] == 1: break
                combo -= 1
        answer += combo
        right += 1
    print(answer)

if __name__ == "__main__":
    main()