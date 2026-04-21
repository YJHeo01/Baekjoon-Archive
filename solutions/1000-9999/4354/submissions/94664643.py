while True:
    s = input()
    if s == '.': break
    length = len(s)
    pi = [0] * length
    j = 0
    answer = 1
    zero_cnt = 1
    for i in range(1,length):
        while j and s[j] != s[i]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
            answer = max(answer,pi[i]//zero_cnt+1)
        else:
            zero_cnt = 1
        if pi[i] == 0: zero_cnt += 1
    print(answer)