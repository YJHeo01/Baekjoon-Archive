while True:
    s = input()
    if s == '.': break
    s_length = len(s)
    pi = [0] * s_length
    j = 0
    for i in range(1,s_length):
        while j and s[j] != s[i]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    word_length = s_length - pi[s_length-1]
    answer = 1
    if pi[s_length-1] % word_length == 0: answer += pi[s_length-1] // word_length
    print(answer)