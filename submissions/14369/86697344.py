def main():
    t = int(input())
    spelling = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    for x in range(1,t+1):
        s = input()
        cnt = {}
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
        y = solution(spelling,cnt,'',0)
        print("Case #"+str(x)+': ' + y)

def solution(spelling,cnt,answer,num):
    if num == 10:
        for c in cnt:
            if cnt[c] != 0: return ''
        return answer
    ret_value = solution(spelling,cnt,answer,num+1)
    if ret_value != '': return ret_value
    num_word = spelling[num]
    max_cnt = 21
    for c in num_word:
        if c not in cnt:
            max_cnt = -1
            break
        max_cnt = min(max_cnt,cnt[c])
    if max_cnt == -1: return ret_value
    tmp = ''
    for _ in range(max_cnt):
        tmp += str(num)
        for c in num_word:
            cnt[c] -= 1
        ret_value = solution(spelling,cnt,answer+tmp,num+1)
        if ret_value != '': return ret_value
    for c in num_word:
        cnt[c] += max_cnt
    return ret_value

if __name__ == "__main__":
    main()
