def main():
    s = list(input())
    cnt = {}
    for c in s:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    answer = 2
    memory = s[0]
    cnt[memory] -= 1
    length = len(s)
    for i in range(1,length):
        c = s[i]
        cnt[c] -= 1
        if memory == c:
            answer += 1   
        else:
            answer += 2
            max_cnt = 0
            for tmp in s:
                max_cnt = max(max_cnt,cnt[tmp])
            if cnt[memory] != max_cnt and max_cnt == cnt[c]:
                memory = c
    print(answer)

if __name__ == "__main__":
    main()